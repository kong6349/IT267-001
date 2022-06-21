#from customer import Customer
#from account import Account
#from bank import customer,account@@@@@

"""from os import access
from oop2.bank import account, customer
"""

""""cus1 = customer.Customer
cus1_acc = account.Account""""

#from bank.customer import Customer
#from bank.account import Account

cus1 = customer.Customer()
cus1.new_customer()

cus1_acc = account.Account()
cus1_acc.open_account(cus1.name,'Saving','10-111-443',500)

print('******Oper Bank Account Detail*******')
print(cus1.cus_info())
print(cus1_acc.display_balance())
