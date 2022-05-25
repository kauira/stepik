from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(int(x))

browser.find_element_by_id('answer').send_keys(y)

browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
button = browser.find_element_by_css_selector('[type="Submit"]')
button.click()


time.sleep(10)

browser.quit()
