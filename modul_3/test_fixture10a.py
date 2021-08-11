
# Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как XPASS
# (“unexpectedly passing” — неожиданно проходит).
# После этого маркировку xfail для теста можно удалить.
# Кстати, к маркировке xfail можно добавлять параметр reason.
# Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx

# Запустим наши тесты коммандой: pytest -rx -v test_fixture10a.py

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

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # reason - Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")