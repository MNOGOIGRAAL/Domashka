import time

def decor(func):
    def wrapper(x):
        start_time = time.time()
        func(x)
        print(f"Вермя выполнения программы{func}:{time.time() - start_time}")
    return wrapper

@decor
def calc_for(number):
    res = []
    for i in range(0, number):
        if i % 2 == 0:
            res.append(i ** 2)
    print(res[-1])
    return res

@decor
def calc_while(number):
    res = []
    y = 0
    i = True
    while i:
        y += 1
        if y >= number:
            print(res[-1])
            i = False
            return res
        elif y % 2 == 0:
            res.append(y ** 2)
    return res

print(calc_for(100000000))
print(calc_while(100000000))