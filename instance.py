class shop:
    shoppint_mall="jamuna"
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]
    def add_to_cart(self,item):
        self.cart.append(item)
mehejabin=shop('meheri')
mehejabin.add_to_cart('jama')        
mehejabin.add_to_cart('juta')        
mehejabin.add_to_cart('burka')
print(mehejabin.cart)

nishu=shop('nishu')
nishu.add_to_cart('watch')
nishu.add_to_cart('t-shart')
nishu.add_to_cart('pent')
print(nishu.cart)