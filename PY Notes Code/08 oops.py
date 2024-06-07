# class Student:
#     name = "aman"
# s1 = Student()
# print(s1.name)

class Launda:
    def __init__(self, fullname, jaati):
        self.name = fullname
        self.jaati = jaati
    def hello(self):
        print("hello", self.name)

s1 = Launda("aman","vishwakarma")
print(s1.name)
print(s1.jaati)
s1.hello()

class Student:
    @staticmethod
    def hello():
        print("hello")
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def avg(self):
        return (self.sub1 + self.sub2 + self.sub3)/3
    
s1 = Student("Aman", 90 , 80 , 100)
print(s1.avg())
s1.hello()

print("acoount management system..")

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self,amount):
        self.balance = self.balance - amount
        print("Rs.", amount , "was debited")
        print("current balance is Rs.", self.get_balance())
    
    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs.", amount , "was credit")
        print("current balance is Rs.", self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000,123)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)