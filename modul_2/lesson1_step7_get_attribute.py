from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//img[contains(@id, "treasure")]')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    # answer = browser.find_element_by_css_selector(".form-control") # По CSS
    # answer = browser.find_element_by_xpath('//label/../input[contains(@id, "answer")]') # По Xpath
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_xpath('//input[contains(@id, "robotsRule")]')
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
