class Laptop:
    def __init__(self,brand,price,colar,memory):
        self.brand=brand
        self.price=price
        self.colar=colar
        self.memory=memory

    def run(self):
        return f'runing the laptop for working'
    def codding(self):
        return f"learning python and  practicing"
class phone:
    def __init__(self,brand,price,colar,dule_sim):
        self.brand=brand
        self.price=price
        self.colar=colar
        self.dule_sim=dule_sim
    def phone_call(self,number,sms):
        return f"Sendign SMS to{number} and massage is {sms}"
    def run(self):
        return f"phone chalanu"
class camera:
    def __init__(self,brand,price,pixel,colar):
        self.brand=brand
        self.price=price
        self.pixel=pixel
        self.colar=colar
        
        
        
        