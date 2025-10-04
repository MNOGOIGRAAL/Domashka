def writing_string(user_str):
    with open("file_1.txt", "a") as file:
        if user_str == "123":
            raise ValueError("Строка = '123'!")
        else:
            file.write(user_str + "\n")

user_value = input("Введите произвольную строку:")
zapis_str(user_value)

#Exception