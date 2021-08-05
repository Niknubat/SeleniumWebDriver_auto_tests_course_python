from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока не появится текст '$100'
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100'))

browser.find_element_by_id("book").click()

x = browser.find_element_by_xpath('//label/*[contains(@id, "input_value")]').text
y = calc(x)

answer = browser.find_element_by_id("answer").send_keys(y)

browser.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

# Копирование числа из алерта в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

time.sleep(2)  # ожидание чтобы визуально оценить результаты прохождения скрипта
browser.quit()  # закрываем браузер после всех манипуляций