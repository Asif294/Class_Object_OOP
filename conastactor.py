class Phone:
    manufacture='china'

    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price

    def send_massage(self,phone,sms):
        text=f"Sending number is : {phone} and massage is {sms}"
        print(text)
my_phone=Phone("kala chan",'iphone',120000)
print(my_phone.owner, my_phone.brand,my_phone.price)
her_phone=Phone("dola chan",'oppo',45000)
print(her_phone.owner,her_phone.brand,her_phone.price)


