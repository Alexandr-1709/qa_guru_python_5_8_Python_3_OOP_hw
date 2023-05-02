"""
Протестируйте классы из модуля online_store_model
"""
import pytest

from online_store_model import Product, Cart


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
        assert product.check_quantity(0) is True, 'Ожидается True. quantity продукта больше запрашиваемого'
        assert product.check_quantity(1) is True, 'Ожидается True. quantity продукта больше запрашиваемого'
        assert product.check_quantity(999) is True, 'Ожидается True. quantity продукта больше запрашиваемого'
        assert product.check_quantity(1000) is True, 'Ожидается True. quantity продукта равно запрашиваемому'

    def test_product_check_quantity_negative_value(self, product):
        with pytest.raises(ValueError) as exc_info:
            product.check_quantity(-1)
        assert 'Количество продукта не может быть отрицательным' in str(exc_info.value)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000, 'Не верно определяется quantity после покупки 0 шт. продукта'
        product.buy(1)
        assert product.quantity == 999, 'Не верно определяется quantity после покупки 1 шт. продукта'
        product.buy(200)
        assert product.quantity == 799, 'Не верно определяется quantity после покупки 200 шт. продукта'
        product.buy(799)
        assert product.quantity == 0, 'Не верно определяется quantity после покупки 799 шт. продукта'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001), 'Ожидаемая ошибка ValueError, не была вызвана'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        assert len(cart.products) == 0, 'До добавления продуктов, корзина должна быть пустой'
        cart.add_product(product)
        assert len(cart.products) == 1, 'В корзине должно находиться одно наименование товара'
        assert cart.products[
                   product] == 1, 'Не верное количество товара. При добавлении по умолчанию количество равно 1'
        cart.add_product(product, 100)
        assert cart.products[product] == 101

    def test_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 3)
        assert cart.products[product] == 7, 'Ошибка вычисления количества, после удаления 3 шт. продукта'
        cart.remove_product(product)
        assert len(cart.products) == 0, 'Если количество не указано, то удаляется вся позиция'
        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert cart.products[product] == 0, 'Ошибка вычисления, после удаления всго количества продукта'
        cart.add_product(product, 500)
        cart.remove_product(product, 501)
        assert len(cart.products) == 0, 'Если указаное количество больше чем в корзине, то удаляется вся позиция'

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 100)
        cart.clear()
        assert len(cart.products) == 0, 'Корзина не очищена'

    def test_get_total_price(self, cart, product):
        assert cart.get_total_price() == 0, 'При пустой корзине стоимость товаров равна 0'
        cart.add_product(product)
        assert cart.get_total_price() == 100, 'Ошибка вычисления стоимости товара в корзине'
        cart.add_product(product, 50)
        assert cart.get_total_price() == 5100, 'Ошибка вычисления стоимости товара в корзине'

    def test__buy_product(self, cart, product):
        cart.add_product(product, 100)
        cart.buy()
        assert len(cart.products) == 0, 'После покупки товара, корзина очищается'

    def test_product_buy_more_than_available(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy(), 'Ожидаемая ошибка ValueError, не была вызвана'
