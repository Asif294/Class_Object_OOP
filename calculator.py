class Calculator:
    brand="cassio"
    def add(num_1,num_2):
        add_n=num_1+num_2
        return add_n
    def sub(num_1,num_2):
        res=num_1-num_2
        return res
    def mul(num_1,num_2):
        muleti=num_1*num_2
        return muleti
    def divi(num_1,num_2):
        div=num_1/num_2
        return div
my_claculator=Calculator
adding=my_claculator.add(44,44)
print(adding)
sub=my_claculator.sub(55, 44)
print(sub)
mul=my_claculator.mul(44 ,5)
print(mul)
div=my_claculator.divi(40,3)
print(div)