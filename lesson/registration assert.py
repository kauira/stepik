import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    input_1 = browser.find_element(by=By.CSS_SELECTOR, value="input.first:required")
    input_1.send_keys("nope")

    input_2 = browser.find_element(by=By.CSS_SELECTOR, value="input.second[required]")
    input_2.send_keys("nope")

    input_3 = browser.find_element(by=By.CSS_SELECTOR, value="input.third[required]")
    input_3.send_keys("nope")
    #nec_inputs = browser.find_elements(by=By.CSS_SELECTOR, value="div.first_block input")
    #for input in nec_inputs:
        #input.send_keys("nope")

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(by=By.TAG_NAME, value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(5)

    browser.quit()
