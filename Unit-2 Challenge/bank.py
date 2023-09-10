class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number  
        self.__account_holder_name = account_holder_name  
        self.__account_balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}")


def create_bank_account():
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, account_holder_name, initial_balance)


account1 = create_bank_account()
while True:
    a=input("Enter the options---[1:Display balance ,2:Deposit ,3:Withdraw]")
    if int(a)==1:
        account1.display_balance()
    elif int(a)==2:
        b=float(input("Enter amount to be deposited: "))
        account1.deposit(b)
    elif int(a)==3: 
        c=float(input("Enter amount to be withdrawn: "))
        account1.withdraw(c)
        account1.display_balance()
    else: 
        print("Thank you for banking with us, have a nice day:)")
        break
        





