import time

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    time.sleep(2)

# Комманды для запуска разных браузеров(тестов в браузерах) из командной строки:
# pytest -s -v --browser_name=chrome test_parser.py
# pytest -s -v --browser_name=firefox test_parser.py