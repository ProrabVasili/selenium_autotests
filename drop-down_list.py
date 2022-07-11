from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

def value_text(x):
    return int(browser.find_element(By.ID, x).text)


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects2.html')

    sum = value_text('num1')+value_text('num2')


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{sum}")

    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()


finally:
    sleep(15)
    browser.quit()