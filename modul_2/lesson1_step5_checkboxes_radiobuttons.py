from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//label/*[contains(@id, "input_value")]')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    # answer = browser.find_element_by_css_selector(".form-control") # По CSS
    # answer = browser.find_element_by_xpath('//label/../input[contains(@id, "answer")]') # По Xpath
    answer.send_keys(y)

    checkbox = browser.find_element_by_xpath('//div/label[contains(text(), "I\'m the robot")]/../input')
    checkbox.click()

    radiobutton = browser.find_element_by_xpath('//div/label[contains(text(), "Robots rule")]/../input')
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
