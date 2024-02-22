from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function to automate newsletter signup process


def newsletter_signup(url, first_name, last_name, email):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Find input fields by name attribute
    first_name_input = driver.find_element(By.NAME, "fName")
    last_name_input = driver.find_element(By.NAME, "lName")
    email_input = driver.find_element(By.NAME, "email")

    # Enter user inputs
    first_name_input.send_keys(first_name)
    last_name_input.send_keys(last_name)
    email_input.send_keys(email)

    # Find and click the "Sign Up" button
    sign_up_button = driver.find_element(By.CSS_SELECTOR, "form button")
    sign_up_button.click()


# Call the function with required inputs
newsletter_signup(
    "https://secure-retreat-92358.herokuapp.com/",
    "TestFName", "TestLName", "test@email.com")
