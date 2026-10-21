import pytest


@pytest.fixture()
def browser():
    print("открываем браузер")
    yield "Chrome"
    print("закрываем браузер")


@pytest.fixture()
def get_admin():
    return 5


def test(get_admin, browser):
    assert get_admin == 5
    assert browser == "Chrome"
    assert 1 == 1


print('Я', 'учусь', 'программировать', 'на', 'Python!')
