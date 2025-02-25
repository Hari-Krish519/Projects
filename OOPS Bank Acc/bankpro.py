class BalException(Exception):
    pass
class BankAccount:
    def __init__(self, initial_amount, acc_name):
        self.balance = initial_amount
        self.name = acc_name
        print(f"\nAccount '{self.name}' was created. \nAccount Balance is {self.balance:.2f}")

    def acc_balance(self):
        print(f"\nAccount Holder Name:\t '{self.name}'\nYour Account Balance:\t {self.balance:.2f}")
        
    def dep_amount(self, amount):
        self.balance = self.balance + amount
        print("Deposit Complete")
        self.acc_balance()
    
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalException(
                f"\nSorry account '{self.name}' only has a balance of {self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw Complete")
            self.acc_balance()
        except BalException as error:
            print(f"\nWirhdraw interrupted: {error}")
    
    def transfer(self, account, amount):
        try:
            print(f"\n Transfer in Progress")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.dep_amount(amount)
            print(f"\nTransfer Completed ✅")
        
        except BalException as error:
            print(f"\n Transfer Interrupted ❌: {error}")
    
class InterestAccount(BankAccount):
    def dep_amount(self, amount):
        self.balance = self.balance + (amount * 1.04)
        print("Deposit Completed")
        self.acc_balance()
        
class SavingAccount(InterestAccount):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 50
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw Completed")
            self.acc_balance()
        except BalException as error:
            print(f"\nWirhdraw interrupted: {error}")

    


