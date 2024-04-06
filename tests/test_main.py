import pytest

from classes.category import Category
from classes.product import Product
from classes.smartphone import SmartPhone


@pytest.fixture()
def product_iphone():
    return Product('Iphone 15', '512Gb, Gray space', 210000.0, 8)


@pytest.fixture()
def product_intel():
    return Product('i514500', 'L1 16Mb, L2 32Mb, L3 64Mb', 30000.0, 15)


@pytest.fixture()
def category_smartphones():
    return Category('Smartphones', 'Smarter than humans',
                    [Product('Iphone 15', '512Gb, Gray space', 210000.0, 8),
                     Product('Galaxy 10', '256GB, Green', 150000.0, 5)])


@pytest.fixture()
def adding_products():
    data_for_product = {
        'name': 'Iphone 15 Pro',
        'description': '512Gb Red',
        'price': 250000.0,
        'quantity': 5
    }
    return Product.creating_product(data_for_product)


@pytest.fixture()
def smartphone_iphone():
    return SmartPhone('Apple', 'Device with bited apple', 160000, 10, 2.65, 'iPhone 11', 256, 'Black')


def test_product_init(product_iphone):
    assert product_iphone.name == 'Iphone 15'
    assert product_iphone.description == '512Gb, Gray space'
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_product_init_2(product_intel):
    assert product_intel.name == 'i514500'
    assert product_intel.description == 'L1 16Mb, L2 32Mb, L3 64Mb'
    assert product_intel.price == 30000.0
    assert product_intel.quantity == 15


def test_category_init(category_smartphones):
    assert category_smartphones.name == 'Smartphones'
    assert category_smartphones.description == 'Smarter than humans'
    assert category_smartphones.all_quantity_category == 1
    assert category_smartphones.all_quantity_unique_product == 2
    assert (category_smartphones.getting_list_of_product ==
            'Iphone 15, 210000.0 руб. Остаток: 8 шт.Galaxy 10, 150000.0 руб. Остаток: 5 шт.')


def test_adding_products(adding_products):
    data_for_product = {
        'name': 'Iphone 15 Pro',
        'description': '512Gb Red',
        'price': 250000.0,
        'quantity': 5
    }
    assert Product.creating_product(data_for_product)


def test_category_print(category_smartphones):
    assert category_smartphones.__str__() == 'Smartphones, количество продуктов: 13 шт.'


def test_product_print(product_iphone):
    assert product_iphone.__str__() == 'Iphone 15, 210000.0 руб. Остаток: 8.'


def test_product_add(product_iphone, product_intel):
    assert product_iphone + product_intel == 2_130_000.0
    with pytest.raises(TypeError):
        assert product_iphone + smartphone_iphone


def test_smartphone_init(smartphone_iphone):
    assert smartphone_iphone.name == 'Apple'
    assert smartphone_iphone.description == 'Device with bited apple'
    assert smartphone_iphone.price == 160000.0
    assert smartphone_iphone.quantity == 10
    assert smartphone_iphone.performance == 2.65
    assert smartphone_iphone.model == 'iPhone 11'
    assert smartphone_iphone.memory == 256
    assert smartphone_iphone.color == 'Black'


def test_product_repr(smartphone_iphone):
    assert smartphone_iphone.__repr__() == "SmartPhone['Apple', 'Device with bited apple', 160000.0, 10, 2.65, 'iPhone 11', 256, 'Black']"
