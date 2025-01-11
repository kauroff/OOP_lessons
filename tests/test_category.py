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


def test_category_init(category):
    assert category.name == 'Шкафы'
    assert category.desc == 'Напольные шкафы'
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


@pytest.fixture
def new_product(category):
    category.add_product_in_category({
        "name": "Samsung Galaxy S24",
        "description": "512GB, Серый цвет, 108MP камера",
        "price": 130000.0,
        "quantity": 10
    })


def test_add_product_in_category(category):
    assert category.uniq_products == 6
    assert category.check_products == [{
        "name": "Samsung Galaxy S24",
        "description": "512GB, Серый цвет, 108MP камера",
        "price": 130000.0,
        "quantity": 10
    }]
