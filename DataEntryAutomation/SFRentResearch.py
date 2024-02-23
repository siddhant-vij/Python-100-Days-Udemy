import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_zillow_data():
    url = "https://appbrewery.github.io/Zillow-Clone/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    addresses = [address.text.replace("\n", "").replace(
        "|", "").strip() for address in soup.select(".StyledPropertyCardDataWrapper a address")]

    prices = []
    for price_elem in soup.select(
            ".PropertyCardWrapper__StyledPriceLine"):
        price_text = price_elem.text.replace(
            "+", "").replace(",", "").replace("$", "").replace("/mo", "").strip()
        if "bd" in price_text:
            price_text = price_text.split(" ")[0].replace(
                ",", "")
        prices.append(int(price_text))

    links = [link["href"]
             for link in soup.select(".StyledPropertyCardDataWrapper a")]

    return addresses, prices, links


def fill_google_form(addresses, prices, links):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    for address, price, link in zip(addresses, prices, links):
        driver.get("Your Google Form Link Here")
        time.sleep(2)
        address_input = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        address_input.send_keys(address)
        price_input.send_keys(str(price))
        link_input.send_keys(link)

        submit_button = driver.find_element(
            by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_button.click()

    driver.quit()


# Usage
addresses, prices, links = scrape_zillow_data()
fill_google_form(addresses, prices, links)
