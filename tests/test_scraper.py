import pytest
from src.scraper import fetch_data, parse_data

def test_fetch_data_returns_html():
    url = "https://example.com"  # You can replace this with a mock URL or test site
    html = fetch_data(url)
    assert html is not None and "<html" in html.lower()

def test_parse_data_extracts_items():
    sample_html = """
    <html>
        <body>
            <div class="item">Item 1</div>
            <div class="item">Item 2</div>
        </body>
    </html>
    """
    result = parse_data(sample_html)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["title"] == "Item 1"
    assert result[1]["title"] == "Item 2"
