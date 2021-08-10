# Мы поместили тестовый сценарий в функцию для разделения тест-кейсов и возможности их независимого запуска.
# Не вдаваясь в подробности, скажем только, что конструкция if __name__ == "__main__" служит для подтверждения того,
# что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля.
# Весь код написанный в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно.


# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")



# Если нам нужно добавить еще один тест, мы можем написать его как функцию в этом же файле.
# В приведенном примере мы уже не увидим сообщение "Everything passed",
# так как падение любого теста вызывает выход из программы:

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")