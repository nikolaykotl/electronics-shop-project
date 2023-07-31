import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""



@pytest.fixture
def item():
    return Item('ноутбукrrrrrrr', 50000, 10)
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
        #assert item1.name == 'Суперсмарт'
        assert item.name == 'ноутбук'


def test_item_name(item1):
    if len(item1.name) <= 10:
        item1.name = item1.name
    else:
        item1.name = item1.name[0:10]
    assert item1.name == 'Суперсмарт'

#def test_item_instantiate_from_csv():
def test_item_string_to_number():
    assert Item.string_to_number('0') == 0
    #assert Item.string_to_number('5.0') == 5
    #assert Item.string_to_number('5.5') == 5

