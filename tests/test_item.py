import pytest
from src.item import Item
from src.phone import Phone

"""Здесь надо написать тесты с использованием pytest для модуля item."""



@pytest.fixture
def item():
    return Item('ноутбук', 50000, 10)
@pytest.fixture
def item1():
    return Item('Суперсмартфон', 20000, 5)

def test_item_calculate_total_price(item):
    assert item.calculate_total_price() == 500000

def test_item_apply_discount(item):
     Item.pay_rate = 0.9
     assert item.apply_discount() == 45000



def test_item_name(item):
    assert item.name == 'ноутбук'

def test_item_name(item1):
    assert item1.name == 'Суперсмарт'


def test_item_name(item):
        if len(item.name) <= 10:
            item.name = item.name
        else:
            item.name = item.name[0:10]

        assert item.name == 'ноутбук'


def test_item_name(item1):
    if len(item1.name) <= 10:
        item1.name = item1.name
    else:
        item1.name = item1.name[0:10]
    assert item1.name == 'Суперсмарт'


def test_item_string_to_number():
    assert Item.string_to_number('0') == 0


def __repr__():
    assert repr(item) == "Item('ноутбук', 50000, 10)"

def __str__():
    assert str(item) == 'ноутбук'

def test_item__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item('Смартфон', 20000, 15)
    assert phone1 + item1 == 20
    assert phone1 + phone1 == 10
    assert item1 + item1 == 30

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2

@pytest.fixture
def phone():
    return Phone("Смартфон", 20000, 5, 3)
    assert phone.number_of_sim == 3
def __repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def __str__():
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 2

def test_number_of_sim(phone):
    assert phone.number_of_sim == 3



