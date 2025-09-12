class shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,item,price,quantity):
        product={"item" : item ,"price":price ,'quantity':quantity}
        self.cart.append(product)
    def chack_out(self,amount):
        total=0
        for item in self.cart:
            total+=item['price'] * item['quantity']
        print(f"tatal price {total}")
        if amount <total:
            print(f"please provide {total-amount}")
        else: 
            print(f"Take your extera money {amount-total}")

shop=shopping("Kalachan ")
shop.add_to_cart('alu',50,5)
shop.add_to_cart('shart',100,4)
shop.add_to_cart('solt',540,6)
print(shop.cart)
shop.chack_out(2000000)

        