from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    sleep(20)
    browser.quit()