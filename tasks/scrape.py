from core.browser import BrowserEngine
from core.utils import timestamp
from core.exporter import export_csv
from config.settings import EXPORTS_DIR, TABLE_URL



def scrape():

    engine = BrowserEngine(headless=False)

    page = engine.start()

    try:


        print("Opening website...... ")

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
        filepath = EXPORTS_DIR / filename

        for record in data:
            print(record)

        export_csv(data, filepath)

        print(f"{len(data)} records scraped")

        page.wait_for_timeout(2000)

    finally:
        engine.stop()




