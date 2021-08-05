from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:

    browser.find_element_by_css_selector('.btn-primary').click()

    first_window = browser.window_handles[0] # Сохранение первой вкладки(на которой находился),
    # что бы можно было вернуться

    # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
    # который возвращает массив имён всех вкладок.
    # Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window) # переключение на вторую вкладку

    x = browser.find_element_by_xpath('//label/*[contains(@id, "input_value")]').text
    y = calc(x)

    answer = browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

finally:
    time.sleep(5)  # ожидание чтобы визуально оценить результаты прохождения скрипта
    browser.quit()  # закрываем браузер после всех манипуляций
