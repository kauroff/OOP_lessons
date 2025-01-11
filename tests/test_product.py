import pytest

from src.product import Product


@pytest.fixture
def products():
    return Product('Яблоки', 'Сезонные', 65.0, 17)


def test_init(products):
    assert products.name == 'Яблоки'
    assert products.desc == 'Сезонные'
    assert products.quantity == 17

# дальше все падает в рекурсию

def test_create_product():
    assert Product.create_product(
        {'name': 'Помидоры', 'desc': 'Азербайджанские', 'price': 230.0, 'quantity': 20}) == None


def test_price(products):
    assert products.price == 65.0


def test_set_price(products):
    assert products.set_price(0) == 'Введена некорректная цена'
    assert products.set_price(100.0) == 100.0


def test_str(products):
    assert products.__str__() == 'Яблоки, 65.0 руб. Остаток: 17 шт.'


def test_add(products):
    tomatoes = Product('Помидоры', 'Азербайджанские', 230.0, 20)
    assert products.__add__(tomatoes) == 5705.0
