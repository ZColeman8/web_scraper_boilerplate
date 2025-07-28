import csv
from src.utils.logger import logger

def save_to_csv(data, file_path="data/output.csv"):
    if not data:
        logger.warning("No data to write.")
        return

    try:
        keys = data[0].keys()
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        logger.info(f"Saved {len(data)} records to {file_path}")
    except Exception as e:
        logger.error(f"Failed to write to CSV: {e}")