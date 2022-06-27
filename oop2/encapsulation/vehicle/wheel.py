from ftplib import ftpcp
from bus import Bus
from motorcycle import Motorcycle

bus = Bus('Bus',4,120,'v124')
#bus.color = 'Blue'
bus.set_color('blue')
#bus.capacity = 34
bus.set_capacity(34)
bus.bus_detail()

bike = Motorcycle('Motorcycle',2,100,'v2223')
#bike.cc = 1200
bike.set_cc(1200)
bike.bike_detail()
