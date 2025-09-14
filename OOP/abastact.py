from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
# Concrete class (implementation)
class Car(Vehicle):
    def start(self):
        return "Car start "
    
    def stop(self):
        return "Car stop"


class Bike(Vehicle):
    def start(self):
        return "Bike started"
    
    def stop(self):
        return "Bike stoped"


car = Car()
bike = Bike()

print(car.start())
print(car.stop())
print(bike.start())
print(bike.stop())
