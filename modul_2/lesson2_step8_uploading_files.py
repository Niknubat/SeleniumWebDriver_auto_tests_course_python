from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector('[name="firstname"]').send_keys("Ivan")
    browser.find_element_by_css_selector('[name="lastname"]').send_keys("Petrov")
    browser.find_element_by_css_selector('[name="email"]').send_keys("s@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test_file_lesson2_step8.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_css_selector('#file').send_keys(file_path)  # Прикрепление файла с помощью кнопки
    time.sleep(1)

    # Отправляем заполненную форму
    browser.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

finally:
    time.sleep(5)  # ожидание чтобы визуально оценить результаты прохождения скрипта
    browser.quit()  # закрываем браузер после всех манипуляций
