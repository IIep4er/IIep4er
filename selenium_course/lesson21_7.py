from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    brow = webdriver.Chrome()
    brow.get(link)

    v1 = brow.find_element_by_id("treasure")
    v1_valuex = v1.get_attribute("valuex")
    f = calc(v1_valuex)

    v2 = brow.find_element_by_id("answer")
    v2.send_keys(f)

    v3 = brow.find_element_by_id("robotCheckbox")
    v3.click()

    v4 = brow.find_element_by_id("robotsRule")
    v4.click()

    v5 = brow.find_element_by_css_selector(".btn.btn-default")
    v5.click()


finally:
    time.sleep(10)
    
    brow.quit()

