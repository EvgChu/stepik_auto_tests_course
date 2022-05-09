from selenium import webdriver
import time
import math
import pytest

# pytest -s -v lesson3/test_lesson3_6_3.py

list_links = {
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
}

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', list_links )
def test_stepic_abswer(browser, link):
    browser.get(link)
    input = browser.find_element_by_css_selector('textarea.ember-text-area')
    answer = str(math.log(int(time.time())))
    input.send_keys(answer)
    # Send answer
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    hidden_text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert hidden_text.split() != "Correct!", hidden_text.split()
