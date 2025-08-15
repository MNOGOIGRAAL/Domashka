class MyMoney:
    lastname = None
    firstname = None
    balance = 0

    def __init__(self, lastname, firstname, balance):
        if balance < 0:
            self.balance = 0
            self.lastname = lastname
            self.firstname = firstname
        else:
            self.lastname = lastname
            self.firstname = firstname
            self.balance = balance

    def BalanceUp(self, plus):
        print("Balance replenishment:", plus)
        self.balance += plus

    def BalanceDown(self, minus):
        if minus > self.balance:
            print("Write-off failed!")
            return None
        else:
            print("Write-off:", "-", minus)
            self.balance -= minus

    def GetBalance(self):
        print("Balance:",self.balance)

data = MyMoney("Igor", "Volkov", 0)

data.GetBalance()
data.BalanceUp(1000)
data.GetBalance()
data.BalanceDown(1001)
data.GetBalance()