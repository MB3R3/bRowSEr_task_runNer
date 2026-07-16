from time import perf_counter

from config.settings import SCREENSHOT_DIR, BASE_URL
from core.utils import ensure_directory, timestamp
from core.browser import BrowserEngine
from core.logger import logger
from core.reports import create_report


def screenshot():

    ensure_directory(SCREENSHOT_DIR)

    engine = BrowserEngine(headless=False)

    page = engine.start()

    start = perf_counter()

    output_file = None

    try:
        logger.info("Screenshot task started")

        print("Opening website.... ")

        page.goto(BASE_URL)

        filename = f"screenshot_{timestamp()}.png"

        output_file = SCREENSHOT_DIR / filename

        print("Taking screenshot...... ")

        page.screenshot(path=str(output_file), full_page=True)

        # print(f"screenshot saved in \n{filepath}")
        duration = perf_counter() - start

        logger.info("screenshot saved sucessfully.")

        report = create_report(task="screenshot", status="Success", duration=duration, output_file=output_file)

        logger.info(f"Report created {report}")

        print(f"Screnshot saved {output_file}")
        print(f"report craeted {report}")

        # page.wait_for_timeout(3000)

    except Exception as e:

        duration = perf_counter() - start

        logger.error(str(e))

        report = create_report(
            task="Screenshot",
            status="Failed",
            duration=duration,
            error=str(e)
        )

        print(f"Error: {e}")
        print(f"Report created: {report}")

    finally:

        engine.stop()
