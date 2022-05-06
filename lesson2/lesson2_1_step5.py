from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    input_answer= browser.find_element_by_css_selector('#answer')
    input_answer.send_keys(calc(x))

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()