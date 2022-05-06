from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    # Ваш код, который заполняет обязательные поля
    x = int(browser.find_element_by_css_selector('#num1').text)
    y = int(browser.find_element_by_css_selector('#num2').text)
    
    select_answer = Select(browser.find_element_by_css_selector('#dropdown'))
    select_answer.select_by_value(str(x+y))

    time.sleep(1)

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