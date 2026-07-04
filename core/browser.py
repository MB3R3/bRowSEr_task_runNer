from playwright.sync_api import sync_playwright


class BrowserEngine:
    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        """Create playwright objects browser, context and page"""
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        return self.page
    

    def stop(self):
        """Ckose all playwright resources without exposing """
        if self.page:
            self.page.close()

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()



    