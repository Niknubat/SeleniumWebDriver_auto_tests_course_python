# В начале поставить плагин pytest-rerunfailures
# Комманда для запуска: pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

# Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:
# "--reruns n", где n — это количество перезапусков.
# Если при повторных запусках тесты пройдут успешно, то и прогон тестов будет считаться успешным.
# Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать проблемные тесты.

# Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста.

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
