from core.browser import BrowserEngine


def open_site():

    engine = BrowserEngine(headless=False)

    page = engine.start()

    print("Opening Practice Site.....")
    page.goto("https://the-internet.herokuapp.com")

    print(f"Page Title: {page.title()}")

    page.wait_for_timeout(3000)

    engine.stop()

    print("Done")
    