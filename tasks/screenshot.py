from config.settings import SCREENSHOT_DIR, BASE_URL
from core.utils import ensure_directory, timestamp
from core.browser import BrowserEngine



def screenshot():

    ensure_directory(SCREENSHOT_DIR)

    engine = BrowserEngine(headless=False)

    page = engine.start()

    try:
        print("Opening website.... ")

        page.goto(BASE_URL)

        filename = f"screenshot_{timestamp()}.png"

        filepath = SCREENSHOT_DIR / filename

        print("Taking screenshot...... ")

        page.screenshot(path=str(filepath), full_page=True)

        print(f"screenshot saved in \n{filepath}")

        page.wait_for_timeout(3000)

    finally:

        engine.stop()
