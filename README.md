# Projects.co.id Project Scraper

## Background

Projects.co.id is an online Indonesian freelancing platform. It helps project owners to find talent to help them with their project. For talents, browsing the website for suitable projects is time consuming. Therefore, this Python script help to scrape all available projects along with detailed information in the website.

## Good Ethical WebScraping

Script user must abide to rules of the website, and use the data for good intention only. And not to perform too many request to the server.

## Requirements

- Python 3.6 or above
- Scrapy

## How To Use

1. Download repository

    ```bash
    git clone https://github.com/ceedadev/projects.co.id-scraper.git

    cd projects.co.id-scraper
    ```

2. (Optional) Install Python Virtual Environment

    ```bash
    python3 -m venv venv
    ```

    - Mac / Linux

    ```bash
    source ./bin/activate
    ```

    - Windows Powershell

    ```bash
    .\venv\Scripts\Activate.ps1
    ```

3. Install requirements

    ```bash
    pip install -r requirements.txt
    ```

4. Run Spider

   - Output CSV

    ```bash
    scrapy crawl projects -O projects.csv
    ```

    - or Output JSON

    ```bash
    scrapy crawl projects -O projects.json
    ```

## Todo

- [x] Implement Scrapy
- [ ] ScrapyRT for API
- [ ] Item Pipelines to SQL DB
- [ ] Perform tracking of projects
- [ ] SMPT Service for new and tracked project tags
