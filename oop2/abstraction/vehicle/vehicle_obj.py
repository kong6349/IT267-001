from vehicle_supclass import *

c = Car('Mazda',220)
c.year = 2021
c.gear = 7
c.seat = 4
c.maintanance = 2022
c.show_detail()
c.show_maintanance()

t = Truck('Isuzu',120)
t.capacity = 2
t.wheel = 8
t.show_detail()
t.show_price()

m = Motocycle('Honda',240)
m.cc = 4
m.model = 'NEW PCX'
m.show_detail()