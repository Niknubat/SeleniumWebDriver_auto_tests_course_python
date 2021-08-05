from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:

    browser.find_element_by_css_selector('.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_xpath('//label/*[contains(@id, "input_value")]')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

finally:
    time.sleep(5)  # ожидание чтобы визуально оценить результаты прохождения скрипта
    browser.quit()  # закрываем браузер после всех манипуляций
