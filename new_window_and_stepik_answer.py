from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def func(x):
    return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    
    browser.switch_to.window(browser.window_handles[1])

    y = func(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    accept = browser.switch_to.alert
    answer = accept.text.split()[-1]
    accept.accept()

    browser.get('https://stepik.org/catalog?auth=login&language=ru')
    sleep(3)
    browser.find_element(By.NAME, 'login').send_keys('your email') #input your email
    browser.find_element(By.NAME, 'password').send_keys('your password') #input you password
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(3)
    browser.get('https://stepik.org/lesson/184253/step/6?unit=158843')
    sleep(7)
    input = browser.find_element(By.TAG_NAME, 'textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input) 
    input.send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

finally:
    sleep(5)
