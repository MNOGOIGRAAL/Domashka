def counting(user_word, table):
    up_word = user_word.upper()
    total_sum = 0
    for i in up_word:
        for j in table.keys():
            if i in table[j]:
                total_sum = total_sum + j
    print(f"Стоимость слова: {total_sum}")




value_table = {1: ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
               2: ["Д", "К", "Л", "М", "П", "У"],
               3: ["Б", "Г", "Ё", "Ь", "Я"],
               4: ["Й", "Ы"],
               5: ["Ж", "З", "Х", "Ц", "Ч"],
               8: ["Ш", "Э", "Ю"],
               10: ["Ф", "Щ", "Ъ"]}

user_word = input("Введите слово:")
counting(user_word, value_table)