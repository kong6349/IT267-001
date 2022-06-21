from cusoder.customer import Customer
from cusoder.order import Order

cus1 = Customer('Jame','Nontaburi')

order1 = Order('15-06-2022','packed')

print(f'Order of {cus1.name} on {order1.date} is {order1.status}')
