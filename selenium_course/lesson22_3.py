from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    brow = webdriver.Chrome()
    brow.get(link)

    num1 = brow.find_element_by_id("num1")
    num1 = int(num1.text)
    num2 = brow.find_element_by_id("num2")
    num2 = int(num2.text)

    summ = str(num1 + num2)
    print(summ)

    select = Select(brow.find_element_by_tag_name("select"))
    select.select_by_visible_text(summ)

    brow.find_element_by_css_selector(".btn.btn-default").click()




finally:
    time.sleep(10)
    
    brow.quit()