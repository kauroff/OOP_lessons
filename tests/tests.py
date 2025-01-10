import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category():
    return Category('Шкафы', 'Напольные шкафы', ['1', '2', '3'])


def test_category_init(category):
    assert category.name == 'Шкафы'
    assert category.desc == 'Напольные шкафы'


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


@pytest.fixture
def products():
    return Product('Яблоки', 'Сезонные', 65.0, 17)


def test_init(products):
    assert products.name == 'Яблоки'
    assert products.desc == 'Сезонные'
    assert products.quantity == 17
