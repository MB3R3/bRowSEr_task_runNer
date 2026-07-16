from time import perf_counter

from core.browser import BrowserEngine
from config.settings import DOWNLOAD_URL, DOWNLOAD_DIR
from core.utils import ensure_directory
from core.logger import logger
from core.reports import create_report


def download():
    ensure_directory(DOWNLOAD_DIR)
    engine = BrowserEngine(headless=False)

    page = engine.start()

    start = perf_counter()

    output_file = None

    try:
        logger.info('Download starting')

        print("Opening download page...")

        page.goto(DOWNLOAD_URL)

        first_file = page.locator("#content a").nth(5)

        print("Capturing Download File ")
        with page.expect_download() as download_info:
            
            first_file.click()

        download = download_info.value

        filename = download.suggested_filename

        output_file = DOWNLOAD_DIR / filename

        download.save_as(str(output_file))

        duration = perf_counter() - start

        if output_file.exists():
            # print("Downoad Completed Successfully!")
            # print(f"Saved to: \n{filepath}")

            logger.info("Download complete")
            report = create_report(
                task="Download",
                status="Successful",
                duration=duration,
                output_file=output_file
            )
            print("Download Complete! ")
            logger.info(f"Download saved to {output_file}")
            logger.info(f"Report created {report}")

    except Exception as e:

        duration = perf_counter() - start

        report = create_report(
            task="Download",
            status="Failed",
            duration=duration,
            error=str(e)
        )
        logger.info("Download Failed")
        logger.info(f"Report Created {report}")


        # page.wait_for_timeout(2000)

    finally:
        engine.stop()



