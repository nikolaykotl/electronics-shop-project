import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""



@pytest.fixture
def item():
    return Item('ноутбук', 50000, 10)


def test_item_calculate_total_price(item):
    assert item.calculate_total_price() == 500000

def test_item_apply_discount(item):
     Item.pay_rate = 0.9
     assert item.apply_discount() == 45000
