class Bank:
    def __init__(self,holder_name, initial_deposit):
        self.holder_name=holder_name
        self.__balance=initial_deposit
    def deposti(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
asif=Bank("Asifur rahman",500000000)
asif.deposti(500)
print(asif.get_balance())
        