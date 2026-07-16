import logging

from core.utils import ensure_directory
from config.settings import LOG_DIR, LOG_FILE


ensure_directory(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("broser-task-runner")