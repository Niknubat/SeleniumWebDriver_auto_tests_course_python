# Пропуск тестов

# В PyTest есть стандартные метки, которые позволяют пропустить тест
# при сборе тестов для запуска (то есть не запускать тест) или запустить,
# но отметить особенным статусом тот тест, который ожидаемо упадёт из-за наличия бага,
# чтобы он не влиял на результаты прогона всех тестов. Эти метки не требуют дополнительного объявления в pytest.ini
# Чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip
# pytest -s -v test_fixture8_2.py

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")