from pathlib import Path


BASE_URL = "https://the-internet.herokuapp.com"

LOGIN_URL = F"{BASE_URL}/login"

USERNAME = "tomsmith"

PASSWORD = "SuperSecretPassword!"


OUTPUT_DIR = Path("outputs")
SCREENSHOT_DIR = OUTPUT_DIR / "screenshots"


EXPORTS_DIR = OUTPUT_DIR / "exports"
TABLE_URL = f"{BASE_URL}/tables"
