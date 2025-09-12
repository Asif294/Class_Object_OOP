class Phone:
    print=3000
    brand='Samsung'
    color='black'
    feture=['camera','lance','charger']

    def call(self):
        print("Calling one person !")
    def send_sms(self,number,sms):
        text=f"Sending sms to : {number} and massage is : {sms}"
        return text

my_phone=Phone()
result=my_phone.send_sms(1885430525,'i dont miss you')
print(result)
