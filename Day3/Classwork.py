# %%
even_odd = lambda n: "Even" if n%2 ==0 else "Odd"
print(even_odd(5))

# %%
is_float = lambda x: "Float" if type(x) ==float else "Not float"
print(is_float(10.5))

# %%
#WAP to find the sum of 3 numbers
sum_3 = lambda x,y,z:x+y+z
print(sum_3(10,21,54))

# %%
x=10
def show_value():
    global x
    x+=10
    print("Inside function",x)

show_value()
print("Outside function",x)

# %%
def demo():
    a=5
    print(a)

demo()
#print(a) will give error because a is defined within the function

# %%
def outer():
    x=10
    def inner():
        nonlocal x
        x+=5
    inner()
    print(x)
outer()

# %%

class Bank:
    Bankname = "HDFC"
    IFSC = "HDFC813209"
    Location = "Shivnarayanpur"
    Timing = "10am - 4pm"
Sunny = Bank()
Sunny.bankaccount = "123001"
Sunny.address = "Begusarai"
Sunny.mobile = "7361000001"
Piyush = Bank()
Piyush.bankaccount = "123002"
Piyush.address = "Patna"
Piyush.mobile = "7361000002"
Tarun = Bank()
Tarun.bankaccount = "123003"
Tarun.address = "Delhi"
Tarun.mobile = "7361000003"

print("Bank Name:", Bank.Bankname)
print("IFSC:", Bank.IFSC)
print()

print("Sunny Details:", Sunny.bankaccount, Sunny.address, Sunny.mobile)
print("Piyush Details:", Piyush.bankaccount, Piyush.address, Piyush.mobile)
print("Tarun Details:", Tarun.bankaccount, Tarun.address, Tarun.mobile)

# %%
class Bank:
    Bankname = "HDFC"
    IFSC = "HDFC813209"
    Location = "Shivnarayanpur"
    Timing = "10am - 4pm"
    def set_details(obj, name, age, phone, pan, balance):
        obj.name=name
        obj.age=age
        obj.phone=phone
        obj.pan=pan
        obj.balance=balance

o1=Bank()
o2=Bank()
o1.set_details("tarun",22,9879,"Kxop854j",4000)
o2.set_details("piyush",21,9889,"asjs67jk",4500)

print(o2.balance)

# %%
class Bank:
    Bankname = "HDFC"
    IFSC = "HDFC813209"
    Location = "Shivnarayanpur"
    Timing = "10am - 4pm"

    def __init__(self,name,age,phone,pancard,balance):
        self.name=name
        self.age=age
        self.phone=phone
        self.pancard=pancard
        self.balance=balance

c1=Bank("Sunny",21,967489933,"kxopk6964f",39000)
c2=Bank("Tarun",22,95743393,"Lthpk9438h",20000)
print(c1.balance,c1.Bankname)
print(c2.phone)
print(Bank.IFSC)

# %%
class Bank:
    Bankname = "HDFC"
    IFSC = "HDFC813209"
    Location = "Shivnarayanpur"
    Timing = "10am - 4pm"

    def __init__(self,name,age,phone,pancard,balance):
        self.name=name
        self.age=age
        self.phone=phone
        self.pancard=pancard
        self.balance=balance
    def display(self):
        print(self.name, self.phone, self.balance)

    def change_phone(self, new_phone):
        self.phone=new_phone

    def withdraw_money(self, wmoney):
        if(wmoney<0):
            print("Invalid amount")
        elif(wmoney>self.balance):
            print("Insufficient Balance")
        elif(wmoney<self.balance):
            self.balance=self.balance-wmoney
            print(f"{wmoney} withdrawn from your account\nAvailable balance is :{self.balance}")
        else:
            print("Invalid input")
        

o1=Bank("Piyush",22,95949,"dfjksd",40000)

o1.withdraw_money(100) 

# %%
class Bank:
    Bankname = "HDFC"
    IFSC = "HDFC813209"
    Location = "Shivnarayanpur"
    Timing = "10am - 4pm"

    def __init__(self,name,age,phone,pancard,balance):
        self.name=name
        self.age=age
        self.phone=phone
        self.pancard=pancard
        self.balance=balance
    def display(self):
        print(self.name, self.phone, self.balance,self.Location)

    def change_phone(self, new_phone):
        self.phone=new_phone
    @classmethod
    def change_location(self,Location):
        self.Location=Location
obj1=Bank("Manyata Manas",22,6206092501,"ghdgd",10800)
obj1.change_location("COIMBATORE")


o1=Bank("Piyush",22,95949,"dfjksd",40000)


obj1.display()



