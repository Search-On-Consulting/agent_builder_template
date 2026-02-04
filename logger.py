import logging
import os

ENV = os.environ.get("ENV", "development")

logging.basicConfig(
    level=logging.ERROR if ENV.lower() == "production" else logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)
