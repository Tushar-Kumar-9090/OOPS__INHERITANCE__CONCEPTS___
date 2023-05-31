

#*-------------------------------------------------------------------------------------------------------
##                                          Single Inheritance
#*-------------------------------------------------------------------------------------------------------

## Bank Application(Bank_v1 and Bank_v2)



class Bank_v1:
    Bank_name='SBI'
    Bank_roi=7
    Bank_branch="Hydrabad"

    def __init__(self,name,age,account,balance):
        self.name=name
        self.age=age
        self.account=account
        self.balance=balance

    @classmethod
    def bank_details(cls):
        print(f"Bank Name Is {cls.Bank_name}")
        print(f"Bank ROI Is {cls.Bank_roi}")
        print(f"Bank Branch Is {cls.Bank_branch}")

    @staticmethod
    def get_int_value():
        value=int(input("Enter The Value: "))
        return value

    def withdraw(self):
        amount=self.get_int_value()
        if self.balance>=amount:
            self.balance-=amount
            print(f"Withdraw Successful And Remaining Balance Is {self.balance}")
        else:
            print("Insufficient Balance")

    def deposite(self):
        amount=self.get_int_value()
        self.balance+=amount
        print(f"Deposite Successful And Remaining Balance Is {self.balance}")

class Bank_v2(Bank_v1):
    Bank_branch="Bengaluru"
    Bank_IFSC="SBIN0010125"

    def customer_details(self):
        print(f"Customer Name Is {self.name}")
        print(f"Customer Age Is {self.age}")
        print(f"Customer Account Number Is {self.account}")
        print(f"Customer Balance Is {self.balance}")
    
    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_value()
        cls.Bank_roi=newroi
        print(f"Updated ROI Is {cls.Bank_roi}")

obj2=Bank_v1("Tushar",25,36209,50000)
obj1=Bank_v2("Tushar",25,36209,50000)
obj1.customer_details()
Bank_v2.customer_details(obj1)
obj1.bank_details()
obj1.withdraw()
obj1.withdraw()
obj1.deposite()
obj2.bank_details()
obj1.bank_details()
obj1.change_roi()











#*-------------------------------------------------------------------------------------------------------
##                                          Multiple Inheritance
#*-------------------------------------------------------------------------------------------------------

class Father:
    car='nano car'
    bike='chetak bike'
    cycle='Hero cycle'

class Mother:
    bike:'scooty'
    cycle='ladies cycle'

class Son1(Mother,Father):
    bike='Pulser220f'

class Son2(Father,Mother):
    bike='Dominar'

print(Son1.mro())
s1=Son1()
print(s1.bike)
print(s1.cycle)
print(s1.car)

print(Son2.mro())
s2=Son2()
print(s2.bike)
print(s2.cycle)
print(s2.car)




#*-------------------------------------------------------------------------------------------------------
##                                          Hirarchial Inheritance
#*-------------------------------------------------------------------------------------------------------

class Father:
    car='nano car'
    bike='chetak bike'
    cycle='Hero cycle'


class Son1(Father):
    bike='Pulser220f'

class Son2(Father):
    bike='Dominar'

print(Son1.mro())
s1=Son1()
print(s1.bike)
print(s1.cycle)
print(s1.car)

print(Son2.mro())
s2=Son2()
print(s2.bike)
print(s2.cycle)
print(s2.car)



#*-------------------------------------------------------------------------------------------------------
##                                          Multilevel Inheritance
#*-------------------------------------------------------------------------------------------------------
class Bank_v1:
    bank_name='SBI'
    bank_branch='Marathali'
    bank_roi=7

    def __init__(self,n,a,acc,balan):
        self.name=n
        self.age=a
        self.account=acc
        self.balance=balan

    def customer_details(self):
        print(f'Name of the customer is {self.name}')
        print(f'Age of the customer is {self.age}')
        print(f'Account Number of the customer is {self.account}')
        print(f'Balance of the customer is {self.balance}')

class Bank_v2(Bank_v1):
    bank_branch='Bengaluru'
    bank_ifsc="SBIN0010125"

    def __init__(self,n,a,ac,bal,pin):
        super().__init__(n,a,ac,bal)
        self.pin=pin

class Bank_v3(Bank_v2):
    def __init__(self,name,age,account,balance,pin,adhar):
        super().__init__(name,age,account,balance,pin)
        self.adhar=adhar
    
    def customer_details(self):
        super().customer_details()
        print(f'Adhar of the customer is {self.adhar}')

tushar=Bank_v3("Tushar",25,36209,10000,9090,877764806367)
tushar.customer_details()

