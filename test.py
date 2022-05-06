from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    time.sleep(1)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()
except:
    time.sleep(2)
        # закрываем браузер после всех манипуляций
    browser.quit()