from core.browser import BrowserEngine
from config.settings import DOWNLOAD_URL, DOWNLOAD_DIR
from core.utils import ensure_directory


def download():
    ensure_directory(DOWNLOAD_DIR)
    engine = BrowserEngine(headless=False)

    page = engine.start()

    try:
        print("Opening download page...")

        page.goto(DOWNLOAD_URL)

        first_file = page.locator("#content a").nth(4)

        with page.expect_download() as download_info:
            
            first_file.click()

        download = download_info.value

        filename = download.suggested_filename

        filepath = DOWNLOAD_DIR / filename

        download.save_as(str(filepath))

        if filepath.exists():
            print("Downoad Completed Successfully!")
            print(f"Saved to: \n{filepath}")

        else:

            print("Download Failed")

        page.wait_for_timeout(2000)

    finally:
        engine.stop()




