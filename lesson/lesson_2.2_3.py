from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('num1').text
x = int(x_element)
y_element = browser.find_element_by_id('num2').text
y = int(y_element)
z = x + y

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(f"{z}")

browser.find_element_by_css_selector('[type="Submit"]').click()

time.sleep(10)

browser.quit()