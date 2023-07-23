"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        pos_quantity = product.quantity
        assert product.check_quantity(pos_quantity), 'ошибка quantity равно product.quantity'

        less_than_quantity = product.quantity - 10
        assert product.check_quantity(less_than_quantity), 'ошибка quantity меньше product.quantity'

        more_than_quantity = product.quantity + 10
        assert not product.check_quantity(more_than_quantity), 'ошибка quantity больше product.quantity'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        buy_all = product.quantity
        product.buy(buy_all)
        assert product.quantity == 0, 'failed buy all'

        buy_less = product.quantity -10
        product.buy(buy_less)
        assert product.quantity == 10, 'failed buy less'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(product.quantity + 1) is ValueError, 'failed buy all'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add(self, product, cart):
        cart.add_product(product, 15)
        assert cart.products[product] == 15

        cart.add_product(product, 15)
        assert cart.products[product] == 30

    def test_remove_from_cart(self, product, cart):
        cart.add_product(product, 15)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_from_cart2(self, product, cart):
        cart.add_product(product, 15)
        cart.remove_product(product, 15)
        assert product not in cart.products

    def test_remove_from_cart_more_products(self, product, cart):
        cart.add_product(product, 10)
        cart.remove_product(product, 15)
        assert product not in cart.products

    def test_remove_part_from_cart(self, product, cart):
        cart.add_product(product, 15)
        cart.remove_product(product, 1)
        assert cart.products == {product: 14}

    def test_clear(self, product, cart):
        cart.add_product(product, 15)
        cart.clear()
        assert cart.products == {}

    def test_total_price(self, cart, product):
        cart.add_product(product, 15)
        cart.get_total_price()
        assert cart.get_total_price() == 1500

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

    def test_buy_fail(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()

