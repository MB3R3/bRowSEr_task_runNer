from core.browser import BrowserEngine

def main():
    engine = BrowserEngine(headless=False)

    print("Launching Brower.........")
    
    page = engine.start()

    page.goto("https://the-internet.herokuapp.com")

    print("Page title")

    print(page.title())

    page.wait_for_timeout(3000)

    engine.stop()

    print("Browser closed")





if __name__ == "__main__":
    main()