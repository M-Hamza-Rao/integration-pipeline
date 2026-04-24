import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_success(email: str):
    logging.info(f"SUCCESS: {email}")

def log_failure(email: str):
    logging.error(f"FAILED: {email}")

def log_retry(email: str, attempt: int):
    logging.warning(f"RETRY {attempt}: {email}")