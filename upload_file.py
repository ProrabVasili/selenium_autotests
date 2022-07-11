import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'just.txt')           

def input_text(name, text):
    browser.find_element(By.CSS_SELECTOR, f'[name="{name}"]').send_keys(text)

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    input_text('firstname','Melkiy')
    input_text('lastname', 'Shakarapet')
    input_text('email', 'melkiy@gmail.com')

    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    
finally:
    sleep(15)
    browser.quit()