from time import perf_counter

from core.browser import BrowserEngine
from config.settings import BASE_URL, LOGIN_URL, USERNAME, PASSWORD
from core.logger import logger
from core.reports import create_report



def login():

    engine = BrowserEngine(headless=False)

    page = engine.start()

    start = perf_counter()

    output_file = None

    try:
        logger.info("Login action initiated ")

        print("Opening Login Page... ")

        page.goto(LOGIN_URL)

        print("Inputing Username")

        page.fill("#username", USERNAME)

        print("Inputing Password")

        page.fill("#password", PASSWORD)

        print("Submitting Login details")

        page.click("button[type=submit]")

        page.wait_for_load_state("networkidle")

        flash = page.locator("#flash").inner_text()

        duration = perf_counter() - start

        if "You logged into a secure area!" in flash:
            # print("\nLogin successful")
            logger.info("Login successful")
            report = create_report(
                task="Login",
                status="Success",
                duration=duration,
                output_file=output_file
            )

            logger.info(f"Report created {report}")

        
        # else:
    except Exception as e:
        duration = perf_counter() - start

        logger.error(e)

        report = create_report(
            task="Login",
            status="Failed",
            duration=duration,
            error=str(e)
        )
        
        print(f"Error: {e}")
        print(f"Report created: {report}")

        page.wait_for_timeout(3000)


    finally:

        engine.stop()