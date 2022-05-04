from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"),"100"
            )
        )
    browser.find_element_by_css_selector("#book").click()
    y = calc(browser.find_element_by_css_selector("#input_value").text)
    
    browser.find_element_by_css_selector(".form-control").send_keys(y)
    browser.find_element_by_css_selector(".btn#solve").click()




finally:

    time.sleep(5)
    browser.quit()
