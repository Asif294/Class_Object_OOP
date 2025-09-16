class CPU:
    def __init__(self,cores):
        self.cores=cores
class RAM:
    def __init__(self,size):
        self.size=size
class HardDrive:
    def __init__(self,capacity):
        self.capacity=capacity

class Computer:
    def __init__(self,cores,size,capacity):
        self.cpu=CPU(cores)
        self.ram=RAM(size)
        self.harddrive=HardDrive(capacity)
        
        
        
        
        