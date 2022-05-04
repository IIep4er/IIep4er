from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_css_selector(".btn").click()
    browser.switch_to_window(browser.window_handles[1])
    y = calc(browser.find_element_by_css_selector("#input_value").text)
    browser.find_element_by_css_selector(".form-control").send_keys(y)
    browser.find_element_by_css_selector(".btn").click()




finally:
    
    time.sleep(5)
   
    browser.quit()