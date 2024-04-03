from classes.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 producing_country: str, period: str, color: str):
        """
        Наследует свойства класса Product и добавляет следующие
        producing_country: страна-производитель
        period: срок прорастания
        color: цвет
        """
        super().__init__(self, name, description, price, quantity)
        self.producing_country = producing_country
        self.period = period
        self.color = color
