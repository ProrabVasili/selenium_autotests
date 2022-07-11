from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def func(x):
    return str(log(abs(12*sin(int(x)))))
    
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    browser.switch_to.alert.accept()
    y = func(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    sleep(20)
    browser.quit()