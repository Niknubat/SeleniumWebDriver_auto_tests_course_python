# Наличие элемента на странице проверил 4 способами(активным оставил способ который мне наиболее понравился)
# Команда смены/выбора языка: pytest --language=es test_items.py

from selenium.common.exceptions import NoSuchElementException  # Для первого способа

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_no_button_shopping_cart(browser):
    browser.get(link)
    browser.implicitly_wait(3)  # Не явное ожидание элементов на странице
    # 1 способ(отлавливаем ошибку NoSuchElementException)
    try:
        browser.find_element_by_css_selector('button.btn-add-to-basket')
    except NoSuchElementException:
        assert False, '!!!ERROR NoSuchElementException:"button.btn-add-to-basket"!!! \
        NO BUTTON "Add to Shopping Cart"'

    # # 2 способ(по селектору ищем все элементы и если их ноль, выводим ошибку)
    # if len(browser.find_elements_by_css_selector('button.btn-add-to-basket')) == 0:
    #     assert True == 0, \
    #     '!!!ERROR NoSuchElementException:"button.btn-add-to-basket"!!! NO BUTTON "Add to Shopping Cart"'
    # else:
    #     button_submit = browser.find_element_by_css_selector("button.btn-add-to-basket")
    #     class_attribute_button = button_submit.get_attribute("class")
    #     assert 'btn-add-to-basket' in class_attribute_button, \
    #     '!!!ERROR NoSuchElementException:"button.btn-add-to-basket"!!! NO BUTTON "Add to Shopping Cart"'

    # # 3 способ - в нем ошибка NoSuchElementException срабатывает быстрее чем  ASSERT(мне не нравится)
    # button_submit = browser.find_element_by_css_selector("button.btn-add-to-basket")
    # class_attribute_button = button_submit.get_attribute("class")
    # assert 'btn-add-to-basket' in class_attribute_button, \
    #     '!!!ERROR NoSuchElementException:"button.btn-add-to-basket"!!! NO BUTTON "Add to Shopping Cart"'

    # # 4 способ - assert обрабатывается оба раза
    # try:
    #     WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    #     button = True
    # except Exception:
    #     button = False
    # assert button, \
    #     '!!!ERROR NoSuchElementException:"button.btn-add-to-basket"!!! NO BUTTON "Add to Shopping Cart"'
