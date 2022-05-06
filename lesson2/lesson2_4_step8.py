import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try: 
  

    browser = webdriver.Chrome()

    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    label = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )

    btn_book = browser.find_element_by_id("book")
    btn_book.click()
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    input_answer= browser.find_element_by_css_selector('#answer')
    input_answer.send_keys(calc(x))

    button = browser.find_element_by_id("solve")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()