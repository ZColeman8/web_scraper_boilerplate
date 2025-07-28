# 🕸️ Web Scraper Boilerplate

This is a reusable Python web scraping boilerplate designed for client projects. It includes structured folders, logging, file output, and testing support using `pytest`.

---

## 🚀 Features

- BeautifulSoup + Requests for scraping
- Modular structure for scalability
- Built-in logging
- Pytest support with config
- CSV output support
- Easy to copy & customize for client work

---

## 🗂️ Folder Structure

```
web_scraper_boilerplate/
├── data/                  # CSV or JSON output
├── logs/                  # Log files
├── src/
│   ├── scraper.py         # fetch_data() & parse_data()
│   └── utils/
│       ├── file_writer.py # save_to_csv() or JSON
│       └── logger.py      # logging setup
├── tests/
│   └── test_scraper.py    # unit tests
├── pytest.ini             # test config
└── README.md              # project info
```

---

## 🧪 How to Run Tests

Just run:

```
pytest
```

> Logging is enabled and console-friendly thanks to `pytest.ini`.

---

## 📝 Logging

- All logs are written to `logs/scraper.log`
- You can change log level or format in `src/utils/logger.py`

---

## 🧰 How to Use

1. Replace the sample logic in `fetch_data()` and `parse_data()` in `src/scraper.py` with your real target.
2. Use `save_to_csv()` from `file_writer.py` to store results.
3. Add more test cases in `tests/test_scraper.py` as needed.

---

## 📦 Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🔁 Reuse

To reuse this for a new project:

1. Duplicate this folder
2. Rename it to the client/project name
3. Replace scraper logic and adapt tests
4. Push to GitHub or Zip for delivery