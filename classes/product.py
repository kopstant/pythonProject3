class Product:
    """
    Класс для продуктов, который имеет атрибуты имени, описания, цены и количества
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Метод для инициализации атрибутов класса Product
        """
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = quantity

    def __str__(self):
        """
        Добавляем строковое отображение в виде:
        Название продукта, цена руб. Остаток: 15 шт.
        """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity}.'

    def __add__(self, other):
        """
        Магический метод для отображения общего баланса
        """
        if type(other) == self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        return 'Нельзя складывать продукты разных типов'

    @classmethod
    def creating_product(cls, product_data: dict):
        return cls(**product_data)

    def adding_product(self, list_of_product):
        """
        Для метода creating_product реализовать проверку наличия такого же товара, схожего по имени.
        В случае если товар уже существует, необходимо сложить количество в наличии старого товара и нового.
        При конфликте цен выбрать ту, которая является более высокой.
        Для этого в метод можно передать список товаров, в котором нужно искать дубликаты.
        """
        for prod in list_of_product:  # Реализуем цикл по списку продуктов
            if prod.name == self.name:  # Если старое имя = новому,то
                prod.quantity += self.quantity  # Добавляем количество в список продуктов.
                if self.__price > prod.__price:  # Если старая цена больше, чем новая, то
                    prod.__price = self.__price  # Обновляем цену на более высокую.

    @property
    def price(self):
        """
        Метод-геттер для атрибута цены
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Метод setter для атрибута цены.
        Принимает новое значение, если цена <= 0 print('Цена введена некорректно'), при этом цена не устанавливается.\
        В случае если цена товара понижается, добавьте логику подтверждения пользователем вручную
        через ввод y(значит yes) или n (значит no) для согласия понизить цену или для отмены действия соответственно.
        """
        if new_price <= 0:
            print('Цена введена некорректно')
        elif new_price > self.__price:
            self.__price = new_price
            print('Цена повышена')
        elif new_price < self.__price:
            user_answer = input('Подтвердите понижение цены: y/n ')
            if user_answer == 'y':
                self.__price = new_price
                print('Цена понижена')
