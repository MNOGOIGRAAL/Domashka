def sorting_data(arr):
    ref_dict = {}
    for i in arr:
        name, goods, number = i.split()
        if name not in ref_dict:
            ref_dict[name] = {}
        if goods not in ref_dict[name]:
            ref_dict[name][goods] = 0
        number = int(number)
        ref_dict[name][goods] += number
    return ref_dict


def data_format(sort_data):
    sort_name = sorted(sort_data.keys())
    total_list = []
    for i in sort_name:
        total_list.append(f"{i}:")
        sort_goods = sorted(sort_data[i].keys())
        for j in sort_goods:
            total_list.append(f"{j} {sort_data[i][j]}")
    print("\n".join(total_list))


values = ["Игорь Тетрадь 3",
          "Михаил Карандаш 3",
          "Виктория Ручка 1",
          "Игорь Карандаш 4",
          "Виктория Скрепка 20",
          "Михаил Карандаш 4",]

res_sort = sorting_data(values)
total = data_format(res_sort)