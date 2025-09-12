class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdrow=100
        self.max_withdrow=100000
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Your balance is {self.balance}")

    def withdrow(self,amount):
        if amount<self.min_withdrow:
            print(f"Fokira you can not withdrow below : {self.min_withdrow}")
        elif amount>self.max_withdrow:
            print(f"bank fokira hoye jabe . you can withdrow maximum {100000}")
        else:
            self.balance-=amount
            print(f"Here is your balance {self.balance}")
islami=Bank(50000)
islami.deposit(1000)
islami.withdrow(50)
print(islami.get_balance())


        