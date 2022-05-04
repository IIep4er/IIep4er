from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
#ввод данных в одинаковые формы 
    v1 = browser.find_elements_by_class_name('form-control')
    for element in v1:
        element.send_keys("Test")

#загрузка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)

#клик кнопки
    v4 = browser.find_element_by_css_selector('.btn.btn-primary')
    v4.click()

finally:
    time.sleep(3)
    
    browser.quit()
    
    