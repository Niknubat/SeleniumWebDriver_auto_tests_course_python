# Задание: пропуск тестов

#Параметр strict
# Ни XFAIL, ни XPASS по умолчанию не приводят к падению всего набора тестов.
# Но это можно изменить, установив параметру strict значение True:
# В этом случае, если тест будет неожиданно пройден (XPASS),
# то это приведет к падению всего тестового набора.
# Запустим наши тесты коммандой: pytest -rX -v test_fixture10b.py

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False