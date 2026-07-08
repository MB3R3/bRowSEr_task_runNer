from core.browser import BrowserEngine
from config.settings import BASE_URL, LOGIN_URL, USERNAME, PASSWORD



def login():

    engine = BrowserEngine(headless=False)

    page = engine.start()

    try:

        print("Opening Login Page........ ")

        page.goto(LOGIN_URL)

        print("Inputing Username")

        page.fill("#username", USERNAME)

        print("Inputing Password")

        page.fill("#password", PASSWORD)

        print("Submitting Login details")

        page.click("button[type=submit]")

        page.wait_for_load_state("networkidle")

        flash = page.locator("#flash").inner_text()

        if "You logged into a secure area!" in flash:
            print("\nLogin successful")

        else:
            print("\nLogin Failed")

        page.wait_for_timeout(3000)


    finally:

        engine.stop()