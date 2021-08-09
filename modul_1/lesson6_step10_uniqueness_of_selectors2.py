from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_xpath('//div/label[contains(text(), "First name")]/../input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div/input[contains(@placeholder, "last")]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//div/input[contains(@placeholder, "email")]')
    input3.send_keys("s@mail.ru")
    # input4 = browser.find_element_by_xpath('//div/input[contains(@placeholder, "phone")]')
    # input4.send_keys("89554695055")
    # input5 = browser.find_element_by_xpath('//div/input[contains(@placeholder, "address")]')
    # input5.send_keys("Нижний Новгород")

    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Текст не соответствует'

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()