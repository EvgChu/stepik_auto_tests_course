from selenium import webdriver
import time 
import unittest

class TestRigister(unittest.TestCase):
    def test_good_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        self._test_link(link)

    def test_bug_link(self):
        link_with_bug = "http://suninjuly.github.io/registration2.html"
        self._test_link(link_with_bug)

    def _test_link(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('input[class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > input')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input[class="form-control third"]')
        input3.send_keys("Petrov@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()