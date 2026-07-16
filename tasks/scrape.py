from time import perf_counter

from core.logger import logger
from core.reports import create_report

from core.browser import BrowserEngine
from core.utils import timestamp
from core.exporter import export_csv
from config.settings import EXPORTS_DIR, TABLE_URL



def scrape():

    engine = BrowserEngine(headless=False)

    page = engine.start()

    start = perf_counter()

    output_file = None

    try:
        logger.info("Initialize Scrapper ")
        print("Opening website...")

        page.goto(TABLE_URL)

        rows = page.locator("#table1 tbody tr ").all()

        data = []

        for row in rows:
            columns = row.locator("td").all_inner_texts()

            records = {
                "Last Name" : columns[0],
                "First Name" : columns[1],
                "Email" : columns[2],
                "Due": columns[3],
                "Website": columns[4]
            }

            data.append(records)
        
        filename = f"user_{timestamp()}.csv"
        output_file = EXPORTS_DIR / filename

        # for record in data:
        #     print(record)

        export_csv(data, output_file)
        duration = perf_counter() - start

        report = create_report(
            task="Scrape",
            status="Success",
            duration=duration,
            output_file=output_file
            )

        logger.info(f"Recoreds saved to {output_file}")
        logger.info(f"Report Created {report}")
        
        print(f"{len(data)} records scraped")

    except Exception as e:

        duration = perf_counter() - start

        report = create_report(
            task="Scrape",
            status="Failure",
            duration=duration,
            error=str(e)
        )
        logger.info("Scraper Failed")
        logger.info(f"Report Created {report}")

        page.wait_for_timeout(2000)

    finally:
        engine.stop()

