from Categories_file import Categories, category1, category2

class Product:
    id_count = 1

    def __init__(self, name, price, category):
        self.__id = Product.id_count
        self.name = name
        self.__price = price
        self.category = category
        Product.id_count += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price <= 0:
            print("Цена не может быть меньше или равна нулю!")
        else:
            self.__price = new_price

    def get_category(self):
        return self.category

    def __str__(self):
        return (f"Product(ID: {self.__id},"
                f"Name: {self.name},"
                f"Price: {self.__price},"
                f"Category: {self.category.get_name()})")


product_samsung = Product("Samsung", 9490, category=category1)
product_sony = Product("Sony", 11990, category=category1)
product_logitech = Product("Logitech", 5490, category=category2)
product_defender = Product("Defender", 4990, category=category2)

# print(product_defender.get_category())
product_sony.set_price(30990)
print(product_sony.get_price())