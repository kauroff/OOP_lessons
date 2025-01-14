import pytest

from src.category import Category


@pytest.fixture
def category():
    return Category('Шкафы', 'Напольные шкафы', [
        {
            "name": "Шкаф",
            "description": "Метр на два",
            "price": 18000.0,
            "quantity": 5
        },
        {
            "name": "Второй шкаф",
            "description": "Полтора на писят",
            "price": 10000.0,
            "quantity": 8
        }])


def test_category_init(category):  # инициализация успешно
    assert category.name == 'Шкафы'
    assert category.desc == 'Напольные шкафы'
    assert category.count_category == 1
    assert category.uniq_products == 2


def test_check_products(category):
    assert category.check_products == [
        {
            "name": "Шкаф",
            "description": "Метр на два",
            "price": 18000.0,
            "quantity": 5
        },
        {
            "name": "Второй шкаф",
            "description": "Полтора на писят",
            "price": 10000.0,
            "quantity": 8
        }]


def test_len(category):
    assert category.__len__() == 13


def test_str(category):
    assert category.__str__() == 'Шкафы, количество продуктов: 13 шт.'


def test_average_price(category):
    assert category.average_price() == 13076.9231
