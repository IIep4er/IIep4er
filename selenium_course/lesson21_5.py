from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('.form-group [id="input_value"]')
    x = x_element.text
    y = calc(x)
    

    value1 = browser.find_element_by_css_selector('.form-group [id="answer"]')
    value1.send_keys(y)
    v2 = browser.find_element_by_id('robotCheckbox')
    v2.click()
    v3 = browser.find_element_by_css_selector('.form-check-input#robotsRule')
    v3.click()
    v4 = browser.find_element_by_css_selector('.btn')
    v4.click()
finally:
    time.sleep(10)
    
    browser.quit()