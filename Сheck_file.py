import random
from datetime import datetime
from Product_file import Product, product_samsung, product_sony, product_defender, product_logitech
from Categories_file import Categories, category1, category2

class Check:
    id_counter = 1
    checksum = {}

    def __init__(self, product):
        self.__id = Check.id_counter
        self.__date = datetime.now()
        self.__checksum = self.__generate_unique_checksum()
        self.product_list = product
        Check.id_counter += 1

    def __generate_unique_checksum(self):
        while True:
            checksum = random.randint(100000, 200000)
            if checksum not in Check.checksum:
                Check.checksum[checksum] = True
                return checksum

    def get_id(self):
        return self.__id

    def get_checksum(self):
        return self.__checksum

    def __str__(self):
        products_info_list = []
        for i in self.product_list:
            products_info_list.append(str(i))
        products_info = ', '.join(products_info_list)

        return (f"Check(ID: {self.__id},\n"
                f"Date: {self.__date},\n"
                f"Checksum: {self.__checksum},\n"
                f"Products: [{products_info}])")

check = Check([product_sony, product_logitech])
print(category1)
print(product_samsung)
print(check)