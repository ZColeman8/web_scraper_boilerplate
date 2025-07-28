import requests
from bs4 import BeautifulSoup
from src.utils.logger import logger

def fetch_data(url):
    logger.info(f"Fetching data from {url}")
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logger.info("Page fetched successfully")
        return response.text
    except Exception as e:
        logger.error(f"Failed to fetch URL: {e}")
        return None

def parse_data(html):
    logger.info("Parsing data...")
    soup = BeautifulSoup(html, "html.parser")
    # Replace the logic below with actual parsing
    data = []
    for item in soup.select("div.item"):  # example selector
        title = item.get_text(strip=True)
        data.append({"title": title})
    logger.info(f"Parsed {len(data)} items")
    return data

def main():
    url = "https://example.com"
    html = fetch_data(url)
    if html:
        data = parse_data(html)
        return data
    return []

if __name__ == "__main__":
    main()