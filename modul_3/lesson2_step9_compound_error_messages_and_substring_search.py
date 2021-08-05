def test_substring(full_string, substring):

    # Проверяем есть ли слово "магазин" в тексте "Поехал в магазин и купил батон"
    # и выводим текст ошибки если это слово отсутствует в строке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

a = 'Поехал в магазин и купил батон'
b = 'магазин'
test_substring(a, b)