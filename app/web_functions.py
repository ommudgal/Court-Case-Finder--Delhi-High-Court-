import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urlextract import URLExtract
import mysql.connector
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self, host=None, user=None, password=None, database=None):
        self.connection = mysql.connector.connect(
            host=host or os.getenv("DB_HOST", "localhost"),
            user=user or os.getenv("MYSQL_USER", "root"),
            password=password or os.getenv("MYSQL_PASSWORD", "rootpass"),
            database=database or os.getenv("MYSQL_DATABASE", "courtdb"),
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()


def get_options(site, id):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(site)
    select_element = driver.find_element(By.NAME, id)
    select = Select(select_element)
    option_list = select.options
    a = []
    for option in option_list:
        a.append(option.text)
    driver.quit()

    return a


def get_pdf_links(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    lenght = Select(driver.find_element(By.NAME, "caseTable_length"))
    lenght.select_by_index(3)

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    table = soup.find("table", {"id": "caseTable"})
    rows = table.find_all("tr")[1:]
    extractor = URLExtract()
    urls = []
    for i in rows:
        url = extractor.find_urls(str(i))
        urls.extend(url)
    driver.quit()
    return urls


def get_case(site, case_type, case_number, case_year):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(site)

    c_number = driver.find_element(By.NAME, "case_number")
    c_type = Select(driver.find_element(By.NAME, "case_type"))
    c_year = Select(driver.find_element(By.NAME, "case_year"))

    c_number.send_keys(case_number)
    c_type.select_by_value(case_type)
    c_year.select_by_value(case_year)

    db = Database()
    db.cursor.execute(
        "INSERT INTO QUERY (query_num, case_type, case_number, case_year) VALUES (%s, %s, %s, %s)",
        (0, case_type, case_number, case_year),
    )
    db.connection.commit()
    db.close()

    capcha_number = driver.find_element(By.CLASS_NAME, "captcha-code")
    driver.find_element(By.NAME, "captchaInput").send_keys(capcha_number.text)

    driver.find_element(By.ID, "search").click()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")

    table = soup.find("table", {"id": "caseTable"})
    rows = table.find_all("tr")[1:]
    extractor = URLExtract()
    urls = []
    for i in rows:
        url = extractor.find_urls(str(i))
        urls.append(url)
    db = Database()
    db.cursor.execute("INSERT INTO RESPONSE (html_table) VALUES (%s)", (table.text,))
    db.connection.commit()
    db.close()

    html_parsing = BeautifulSoup(str(table), "html.parser")

    table2 = html_parsing.find("table")

    headers = [th.text.strip() for th in table2.find_all("th")]

    rows2 = []
    for tr in table2.find_all("tr")[1:]:
        cells = [td.text.strip() for td in tr.find_all("td")]
        rows2.append(cells)

    return headers, rows2[0], get_pdf_links(urls[0][0])
