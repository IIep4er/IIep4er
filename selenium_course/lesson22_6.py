from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #извлекаем текст
    x_element = browser.find_element_by_css_selector('.form-group [id="input_value"]')
    x = x_element.text
    y = calc(x)

    #вводим ответ
    value1 = browser.find_element_by_css_selector('.form-group [id="answer"]')
    value1.send_keys(y)
    
    #чекбокс я робот
    v2 = browser.find_element_by_id('robotCheckbox')
    v2.click()

    #скролим страницу
    browser.execute_script("return arguments[0].scrollIntoView(true);", v2)
    
    #чекбокс робот рулит
    v3 = browser.find_element_by_css_selector('.form-check-input#robotsRule')
    v3.click()
    
    #submit
    v4 = browser.find_element_by_css_selector('.btn')
    v4.click()
finally:
    time.sleep(10)
    
    browser.quit()    