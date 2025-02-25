from bankpro import *

bala = BankAccount(1000, "Balachandra")
ram = BankAccount(2000, "Ram")

bala.acc_balance()
ram.acc_balance()

bala.dep_amount(300)
ram.dep_amount(200)

bala.withdraw(200)
ram.withdraw(100)

bala.transfer(ram, 300)
ram.transfer(bala, 150)

Hari = InterestAccount(300, "Hari")
Hari.acc_balance()
Hari.dep_amount(200)

nandy = SavingAccount(3000, "Nandy")
nandy.withdraw(1000)
nandy.acc_balance()