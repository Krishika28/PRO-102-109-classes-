class Atm:
    def details(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkuserbalance(self):
        print("Your balance is 100000")

    def withdraw(self,amount):
        withdrawl_amount = 100000 - amount
        print("Your withdrawl amount is "+ str(amount))
        print("Amount left in your account"+ str(withdrawl_amount))

def work():
    CardNumber = input("Enter your card no. :- ")
    pinNumber  = input("Enter your pin no. :- ")

    user =  Atm(CardNumber ,pinNumber)

    print("Choose your busniess")
    print("1. Balance Enquriy") 
    print("2. Withdrawl")
    activity = int(input("Enter your business number :- "))

    if (activity == 1):
        user.checkuserbalance()

    elif (activity == 2):
        amount = int(input("Enter the amount:- "))
        user.withdraw(amount)

    else:
        print("Enter a valid number")

work()