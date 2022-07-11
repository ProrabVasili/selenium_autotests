from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def math_func(x):
    return str(log(abs(12*sin(x))))

def click_button(id, elem = By.ID):
    browser.find_element(elem, id).click()


try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')
    
    ans = math_func(int(browser.find_element(By.ID, 'input_value').text))

    browser.find_element(By.ID, 'answer').send_keys(ans)

    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit) 

    click_button('robotCheckbox')
    click_button('robotsRule')
    submit.click()


finally:
    sleep(20)
    browser.quit()
