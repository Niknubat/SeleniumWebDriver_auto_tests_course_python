from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//label/*[contains(@id, "input_value")]')
    x = x_element.text
    y = calc(x)


    # browser.execute_script("window.scrollBy(0, 100);") # Скрол на 100 пикселей вниз
    # answer = browser.find_element_by_id("answer") #
    # browser.execute_script("return arguments[0].scrollIntoView(true);", answer) # Скрол, делаем элемент кликабельным

    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

    answer.send_keys(y)


    checkbox = browser.find_element_by_xpath('//div/label[contains(text(), "I\'m the robot")]/../input')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobutton = browser.find_element_by_xpath('//div/label[contains(text(), "Robots rule")]/../input')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()


    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
