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

    @classmethod
    def creating_product(cls, name, description, price, quantity):
        """
        Метод, который создает товар и возвращает объект,
        который можно добавлять в список товаров
        """
        return cls(name, description, price, quantity)

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
        Принимает новое значение, если цена <= 0 print('Цена введена некорректно'), при этом цена не устанавливается.
        """
        if new_price <= 0:
            print('Цена введена некорректно')
        elif new_price > self.__price:
            self.__price = new_price
        else:
            while True:
                user_answer = input('Подтвердите понижение цены: y/n ')
                if user_answer == 'y':
                    self.__price = new_price
                    print('Цена изменилась')
                    break
                elif user_answer == 'n':
                    print('Цена не изменилась')
                    break
                else:
                    print('Введите один из предложенных вариантов: y/n ')
