from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("My answer!")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    sleep(20)
    browser.quit()
