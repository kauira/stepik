from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('[name="firstname"]').send_keys('Ivan')
browser.find_element_by_css_selector('[name="lastname"]').send_keys('Ivanov')
browser.find_element_by_css_selector('[name="email"]').send_keys('ivam@mail.ru')
element = browser.find_element_by_css_selector("[type='file']")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'Test.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)

browser.find_element_by_css_selector('[type="Submit"]').click()

time.sleep(10)

browser.quit()