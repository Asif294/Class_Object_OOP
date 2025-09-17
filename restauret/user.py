class User():
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address
class Empoloyee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        super().__init__(name, email, phone, address)
        self.age=age
        self.designation=designation
        self.salary=salary
# emp=Empoloyee("Rahim",'rahim@gamil.com',154555,'sherpur',20,'chef',20000)
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.empoloyes=[]## like database 
    def add_empoloyee(self,name,email,phone,address,age,designation,salary):
        empoloye=Empoloyee(name,email,phone,address,age,designation,salary)
        self.empoloyes.append(empoloye)
        print(f"{name} is added !")
    def view_employe(self):
        print("Empoloyee List !")
        for emp in self.empoloyes:
            print(emp.name,emp.email,emp.phone,emp.address)

add=Admin('Admin','admin@gmail.com',52010,'sherpur')
add.add_empoloyee('moinul','asifur@gmail.com',1252,'asherpu',24,'aroiba',4500)



add.view_employe()


        