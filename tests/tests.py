import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category():
    return Category('Шкафы', 'Напольнеы шкафы', ['1', '2', '3'])


def test_init(category):
    assert Category.name == 'Шкафы'
    assert Category.desc == 'Напольные шкафы'
    assert Category.products == ['1', '2', '3']


@pytest.fixture
def new_product():
    Category.add_product_in_category({
        "name": "Samsung Galaxy S24",
        "description": "512GB, Серый цвет, 108MP камера",
        "price": 130000.0,
        "quantity": 10
    })


def test_add_product_in_category(new_product):
    assert Category.uniq_products == 1
    assert Category.check_products == [{
        "name": "Samsung Galaxy S24",
        "description": "512GB, Серый цвет, 108MP камера",
        "price": 130000.0,
        "quantity": 10
    }]


def test_add_product_in_category(category):
    assert Category.name == 'Шкафы'
    assert Category.desc == 'Напольные шкафы'
    assert Category.products == ['1', '2', '3']


@pytest.fixture
def products():
    return Product('Яблоки', 'Сезонные', 65.0, 17)


def test_init(products):
    assert Product.name == 'Яблоки'
    assert Product.desc == 'Сезонные'
    assert Product.price == 65.0
    assert Product.quantity == 17
