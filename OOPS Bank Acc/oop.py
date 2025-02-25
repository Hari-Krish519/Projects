from bankpro import *

jana = BankAccount(1000, "Jana")
ram = BankAccount(2000, "Ram")

jana.acc_balance()
ram.acc_balance()

jana.dep_amount(300)
ram.dep_amount(200)

jana.withdraw(200)
ram.withdraw(100)

jana.transfer(ram, 300)
ram.transfer(jana, 150)

Hari = InterestAccount(300, "Hari")
Hari.acc_balance()
Hari.dep_amount(200)

nandy = SavingAccount(3000, "Nandy")
nandy.withdraw(1000)
nandy.acc_balance()