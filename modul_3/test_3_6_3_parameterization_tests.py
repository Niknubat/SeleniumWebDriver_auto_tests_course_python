# Задание: параметризация тестов

# Для явного ожидания какого либо элемента, нужно использовать следующие импорты:
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By

import time
import math
import pytest
from selenium import webdriver

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']
count_pre = []  # Послания инопланетян


# Фикстура для запуска и закрытия браузера. Для каждой функции свой экземпляр
@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('start_page', links)
def test_link(browser, start_page):
    answer = str(math.log(int(time.time())))
    browser.get(start_page)
    browser.implicitly_wait(30)  # Не явное ожидание элементов на странице
    textarea_answer = browser.find_element_by_css_selector("textarea.ember-text-area")
    textarea_answer.send_keys(answer)
    button_submit = browser.find_element_by_css_selector("button.submit-submission")
    button_submit.click()
    # Для явного ожидания какого либо элемента(указываем какой именно элемент), нужно использовать
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "pre.smart-hints__hint")))
    pre_text_answer = browser.find_element_by_css_selector("pre.smart-hints__hint")
    pre_text = pre_text_answer.text
    if pre_text != "Correct!":
        count_pre.append(pre_text)  # Собираем послания инопланетян
    if start_page == links[-1]:
        print('     ', "Текст для итогового ответа:", "".join(count_pre))  # Вывод полного послания
    assert pre_text == "Correct!", f"Текст ответа: {pre_text} != Ожидаемому результату: 'Correct!'"
