# Конфигурация тестов
# Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py

import pytest
from selenium import webdriver


# Теперь, сколько бы файлов с тестами мы ни создали,
# у тестов будет доступ к фикстуре browser.
# Фикстура передается в тестовый метод в качестве аргумента.
# Таким образом можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
