import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List


class GrowwFund:
    def __init__(self, name: str, url: str, navDate: str, nav: float):
        self.name = name
        self.url = url
        self.navDate = navDate
        self.nav = nav


def extract_data(url: str) -> List[GrowwFund]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    funds_list: List[GrowwFund] = []

    table = soup.find('table', class_='tb10Table')
    if table:
        cards = table.find_all('tr', class_='f22Card')
        for card in cards:
            name_element = card.select_one('.f22SchemeName > div')
            name = name_element.text if name_element else None

            href_element = card.select_one('a')
            href_text = href_element['href']

            fund_url = f"https://groww.in{href_text}"

            url_response = requests.get(fund_url)
            url_soup = BeautifulSoup(url_response.content, 'html.parser')

            nav_date = url_soup.select_one(
                '#fnd2Section > div > div:nth-child(1) > div > table > tr:nth-child(1) > td:nth-child(1)').text.split(": ")[1]
            nav = float(url_soup.select_one(
                '#fnd2Section > div > div:nth-child(1) > div > table > tr:nth-child(1) > td:nth-child(2)').text.split("₹")[1].replace(',', ''))

            funds_list.append(GrowwFund(name, fund_url, nav_date, nav))

    return funds_list


def scrape_groww_funds() -> List[List[GrowwFund]]:
    base_url = "https://groww.in/mutual-funds/filter"
    params = {"q": "", "fundSize": "", "sortBy": 3}
    first_page_url = f"{base_url}?q={params['q']}&fundSize={params['fundSize']}&sortBy={params['sortBy']}"
    funds_list: List[List[GrowwFund]] = []

    funds_list.append(extract_data(first_page_url))

    pagination_text = requests.get(first_page_url).text
    pagination_soup = BeautifulSoup(pagination_text, 'html.parser')
    x = int(pagination_soup.select('.pg1231Container .pg1231Box')[2].text)

    for page_num in range(2, x):
        params['page'] = page_num - 1
        page_url = f"{base_url}?q={params['q']}&fundSize={params['fundSize']}&pageNo={params['page']}&sortBy={params['sortBy']}"
        funds_list.append(extract_data(page_url))

    return funds_list


def flatten_fund_list(funds_list: List[List[GrowwFund]]) -> List[GrowwFund]:
    return [fund for funds in funds_list for fund in funds]


def fill_google_form(funds: List[GrowwFund]) -> None:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    for fund in funds:
        driver.get("Your Google Form Link Here")
        time.sleep(2)
        name_input = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        url_input = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        navDate_input = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        nav_input = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')

        name_input.send_keys(fund.name)
        url_input.send_keys(fund.url)
        navDate_input.send_keys(fund.navDate)
        nav_input.send_keys(str(fund.nav))

        submit_button = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit_button.click()

    driver.quit()


# Usage
fund_list = flatten_fund_list(scrape_groww_funds())
fill_google_form(fund_list)
