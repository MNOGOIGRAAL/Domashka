class Categories:
    id_count = 1

    def __init__(self, name):
        self.__id = Categories.id_count
        self.name = name
        Categories.id_count += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Категория: {self.name}, ID: {self.__id}"

category1 = Categories("Монитор")
category2 = Categories("Клавиатура")
