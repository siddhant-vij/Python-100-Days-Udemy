from selenium import webdriver
from selenium.webdriver.common.by import By


class Event:
    def __init__(self, eventName, eventDate):
        self.eventName = eventName
        self.eventDate = eventDate


def scrape_python_org_for_upcoming_events():
    events = []

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.python.org/")

    menu_items = driver.find_elements(
        By.CSS_SELECTOR, ".event-widget .shrubbery .menu > li")

    for item in menu_items:
        event_name = item.find_element(By.TAG_NAME, "a").text
        date_element = item.find_element(By.TAG_NAME, "time")
        event_date_str = date_element.get_attribute("datetime")
        event_date = event_date_str.split("T")[0]

        event = Event(event_name, event_date)
        events.append(event)

    driver.quit()

    return events


# Usage
upcoming_events = scrape_python_org_for_upcoming_events()
for event in upcoming_events:
    print(event.eventName, event.eventDate)
