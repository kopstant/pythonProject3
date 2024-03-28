from classes.category import Category
from classes.product import Product

data_for_product = {
    'name': 'Iphone 15 Pro',
    'description': '512Gb Red',
    'price': 250000.0,
    'quantity': 5
}

if __name__ == '__main__':
    iphone = Product('Iphone 15', '512Gb, Gray space', 210000.0, 8)
    samsung = Product('Galaxy 10', '256Gb, Green', 150000.0, 5)
    xiaomi = Product('Redmi 5', '128Gb, Red', 64000.0, 15)
    nokia = Product('3310', '8Gb, Smoke', 5000, 100)

    intel = Product('i514500', 'L1 16Mb, L2 32Mb, L3 64Mb', 30000, 15)
    amd = Product('ryzen 6', 'L1 32Mb, L2 32Mb, L3 128Mb', 45000, 45)

    smartphones = Category('Smartphones', 'Smarter than humans', [iphone, samsung, xiaomi, nokia])
    processors = Category('Processors', 'Hotter than the Sun', [intel, amd])

    print(iphone)
    print(smartphones)

    xiaomi.price = 63000.0

    iphone_15_pro = Product.creating_product(data_for_product)
    print(iphone_15_pro)
    print(xiaomi.price)
