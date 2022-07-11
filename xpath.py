from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("My answer")
        
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

finally:
    sleep(20)
    browser.quit()
