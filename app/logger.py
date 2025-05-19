import logging

logger = logging.getLogger("optimizer_logger")
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add handler if not already added
if not logger.hasHandlers():
    logger.addHandler(ch)
