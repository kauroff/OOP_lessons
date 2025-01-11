import pytest

from src.product import Product


@pytest.fixture
def products():
    return Product('Яблоки', 'Сезонные', 65.0, 17)


def test_init(products):
    assert products.name == 'Яблоки'
    assert products.desc == 'Сезонные'
    assert products.quantity == 17
