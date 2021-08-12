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


#   Передача параметров в командной строке
def pytest_addoption(parser):   # встроенная функция pytest_addoption
    # В таком случае в коммандной строке обязательно нужно указывать, какой браузер запустить
    # parser.addoption('--browser_name', action='store', default=None,
                     # help="Choose browser: chrome or firefox")
    # По умолчанию хром - если не вписывать параметр в ком строке
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):   # Фикстура - request. Это все относится "def pytest_addoption(parser):"
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()