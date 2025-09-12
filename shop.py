class shop:
    cart=[]
    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,item):
        self.cart.append(item)
mehezabin=shop('mehejabin')
mehezabin.add_to_cart("shows")
mehezabin.add_to_cart("cloth")
print(mehezabin.cart)

nisho=shop("Nishous")
nisho.add_to_cart("Watch")        
nisho.add_to_cart("Pent")
print(nisho.cart)        