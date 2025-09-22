class MutableString:
    def __init__(self, st, ind, value):
        self.st = st
        self.ind = ind
        self.value = value

    def res_mutable(self):
        bank = []
        for i in self.st:
            bank.append(i)
        print(bank)

        bank[self.ind] = self.value
        print(bank)
        res = ''.join(bank)
        return res


str_1 = MutableString("Hello", 4, "*")
print("Ваша измененая строка:", str_1.res_mutable())