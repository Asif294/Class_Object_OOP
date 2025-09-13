class Vihical:
    def __init__(self,name,price)->None:
        self.name=name
        self.price=price
    def mov(self):
        pass
    def __repr__(self):
        pass
class Bus(Vihical):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price) 

    def __repr__(self):
        return super().__repr__()
    
class Trace(Vihical):
    def __init__(self, name, price,wight): 
        self.wight=wight
        super().__init__(name, price)
    def __repr__(self):
        return super().__repr__()
    
class PickUpTrace(Trace):        #multi-level inheritance 
    def __init__(self, name, price, wight):
        super().__init__(name, price, wight)

#inheritance user ar somoy repr use krote hobe super use korte hobe 
    def __repr__(self):
        return super().__repr__()

class AcBus(Bus):
    def __init__(self, name, price, seat,tempareture):
        self.tempareture=tempareture
        super().__init__(name, price, seat)
    def __repr__(self):
        return f"{self.name} {self.price} {self.seat},{self.tempareture}"
    
greenLine=AcBus('GreenLine',120000000,27,16)
print(greenLine)
