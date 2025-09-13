#inheritance meant its given data from parent class to child class
class Gadget:
    def __init__(self,brand,colar,price,origin):
        self.brand=brand
        self.colar=colar
        self.price=price
        self.origin=origin

    def run(self):
        return f"running deive {self.brand}"
    
class Phone(Gadget):
    def __init__(self, brand,colar,price,origin,duble_sim):
        self.duble_sim=duble_sim
        super().__init__(brand,price,colar,origin)

    def phone_call(self,number,sms):
        return f"sending meaasage in {number} and message is {sms}"
    def __repr__(self)->str:
        return f'phone:{self.brand,self.colar,self.duble_sim}'
    
class laptop:
    def __init__(self,memory,ssd):
        self.memory=memory
        self.ssd=ssd

class camera :
    def __init__(self,pixel):
        self.pixel=pixel
my_phone=Phone('iPhone','blue',120000,'china',True)
print(my_phone)
        
        
        
        