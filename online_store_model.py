class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity


    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError('Продуктов не хватает!')

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count


    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count
        # raise NotImplementedError

    def clear(self):
        self.products.clear()
        # raise NotImplementedError

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price


    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, quantity in self.products.items():
            if not product.check_quantity(quantity):
                raise ValueError(f"Недостаточное количество продукта {product.name}")
            else:
                product.buy(quantity)
        self.clear()


if __name__ == '__main__':
    p1 = Product('мясо', 123.00, 'говядина', 10)
    p2 = Product('хлеб', 34.00, 'батон', 10)
    p3 = Product('крупа', 90.00, 'гречка', 10)
    p4 = Product('сок', 200.00, 'яблочный', 10)
    res = p1.check_quantity(1)
    print(res)
    #p1.buy(2)
    print(p1.quantity)
    cart1 = Cart()
    cart1.add_product(p1, 1)
    cart1.add_product(p2, 2)
    cart1.add_product(p3, 3)
    cart1.add_product(p4, 4)
    print(cart1.get_total_price())
    cart1.remove_product(p2, 1)
    print(cart1.get_total_price())
    cart1.buy()
    print(p1.quantity, p2.quantity, p3.quantity, p4.quantity)


