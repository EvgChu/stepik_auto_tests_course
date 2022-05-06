from selenium import webdriver
import time

link = "http://suninjuly.github.io/cats.html"

try: 
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(link)

    button = browser.find_element_by_id("button")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()