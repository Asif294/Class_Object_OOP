class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print("vat mas mangso khaitese tara")
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team=team
        super().__init__(name, age, height, weight)

    #OverRide
    def eat(self):
        print("vasitable,kathbadam")
    def exerscise(self):
        print("gime a giye tk ses kore ar ki ")

Shakib=Cricketer('shakib',28,35,56,'BD')
Shakib.eat()
Shakib.exerscise()

        