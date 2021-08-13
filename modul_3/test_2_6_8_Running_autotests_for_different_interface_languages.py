# Команда смены/выбора языка: pytest --language=es test_items.py
# Запуск автотестов для разных языков интерфейса
# Браузер передает данные о языке пользователя через запросы к серверу,
# указывая в Headers (заголовке запроса) параметр accept-language

# Если сервер получит запрос с заголовком {accept-language: ru, en},
# то он отобразит пользователю русскоязычный интерфейс сайта.
# Если русский язык не поддерживается, то будет показан следующий язык из списка,
# в данном случае пользователь увидит англоязычный интерфейс

# Чтобы указать язык браузера с помощью WebDriver,
# используйте класс Options и метод add_experimental_option, как указано в примере ниже:

import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# Для Firefox объявление нужного языка будет выглядеть немного иначе:
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)