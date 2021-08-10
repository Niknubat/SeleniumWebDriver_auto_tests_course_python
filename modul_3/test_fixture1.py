# Классические фикстуры (fixtures)

from os import system # Данная строка, для возможности запускать скрипт не из консоли,
# а прямо нажатием на ентер в Пайчарме + к ней идет в самом низу скрипта if __name__ == "__main__":


from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite 1 ..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite 1 ..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("\nstart browser for test 2..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Код ниже, для возможности запускать скрипт не из консоли, а прямо нажатием на ентер в Пайчарме
def main():
    system(f'pytest -sv "{__file__}"')
if __name__ == "__main__":
    main()