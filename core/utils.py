from pathlib import Path
from datetime import datetime


def ensure_directory(directory: Path):
    """
    Create directory if it doesnt exist
    """
    directory.mkdir(parents=True, exist_ok=True)


def timestamp():
    """
    Generate timestamps suitable for filename
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")