from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import log, sin

def math_func(x):
    return str(log(abs(12*sin(x))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click()
    submit = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit) 
    ans = math_func(int(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, "answer").send_keys(ans)
    submit.click()

    accept = browser.switch_to.alert
    answer = accept.text.split()[-1]
    accept.accept()

    browser.get('https://stepik.org/catalog?auth=login&language=ru')
    sleep(3)
    browser.find_element(By.NAME, 'login').send_keys('your email') #input your email
    browser.find_element(By.NAME, 'password').send_keys('your password') #input you password
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(3)
    browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')
    sleep(7)
    input = browser.find_element(By.TAG_NAME, 'textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input) 
    input.send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
 
finally:
    sleep(10)
    browser.quit()