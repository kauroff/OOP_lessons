import pytest
from src.func import Category, Product


@pytest.fixture
def category():
    return Category('Шкафы', 'Напольнеы шкафы', ['1', '2', '3'])


def test_init(category):
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
