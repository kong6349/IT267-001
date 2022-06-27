from turtle import pen
from documentary import Documentary

m = Documentary()
m._add_movie('My Octopus Teacher',2020,'Documentary')
m.add_channel('NetFliex')
m._get_movie()

#superclass (Movie)
print(f'Title: {m._title}')