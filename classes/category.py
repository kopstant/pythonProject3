class Category:
    """
    Класс описывающий категорию продуктов, имеющий атрибуты имени, описания и списка продукции,
    а также счетчик задействованных уникальных продуктов в списке и категорий товаров.
    """
    name: str
    description: str
    products: list
    all_quantity_category = 0
    all_quantity_unique_product = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Метод для инициализации класса Category
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.all_quantity_category += 1     # Подсчитывает категории товаров
        Category.all_quantity_unique_product += len(set(self.__products))   # Подсчитывает уникальные продукты

        self.categories_count = Category.all_quantity_category
        self.product_count = Category.all_quantity_unique_product

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        """
        Добавляем строковое отображение в виде:
        Название категории, количество продуктов.
        """
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def adding_product(self, new_product):
        """
        Метод, который принимает на вход объекта товар и добавляет его в список
        """
        self.__products.append(new_product)
        Category.all_quantity_unique_product += 1

    @property
    def getting_list_of_product(self):
        """
        Геттер, который выводит список товаров в формате:
        Продукт, 'цена' руб. Остаток: '' шт.
        Иными словами - возвращает список с заданными параметрами
        """
        updated_product = ''
        for product in self.__products:
            updated_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
        return updated_product

    @property
    def products(self):
        """
        Метод getter для корректного отображения изменения цены (задание 4)
        """
        return self.__products
