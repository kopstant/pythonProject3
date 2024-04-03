from classes.product import Product


class SmartPhone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: float, model: str, memory: int, color: str):
        """
        Наследует свойства класса Product и добавляет следующие
        performance: производительность
        model: модель
        memory: объем встроенной памяти
        color: цвет
        """
        super().__init__(self, name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self. color = color
