from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return str(int(x)+int(y))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector('#num1')
    num2 = browser.find_element_by_css_selector('#num2')
    x = num1.text
    y = num2.text
    sum_x_y = calc(x, y)

    select = Select(browser.find_element_by_id("dropdown"))
    # select.select_by_value(sum_x_y)  # ищем элемент с текстом из переменной sum_x_y
    select.select_by_visible_text(sum_x_y) # ищет элемент по видимому тексту

    # elements = browser.find_elements_by_css_selector('#dropdown option')
    # value = 0
    # for element in elements:
    #     value += 1
    #     if element.text == sum_x_y:
    #         select.select_by_index(value - 1)  # ищет элемент по его индексу или порядковому номеру


    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
