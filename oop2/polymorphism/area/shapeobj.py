from secrets import choice
from shapetype import *

#Menu
print('======Computer Area========')
print('1) Square')
print('2) Circle')
print('3) Triangle')
choice = int(input('Enter Choice (1-3): '))
print('===========================')

if choice ==1:
    s = Square()
    s.length = float(input('Enter lenth: '))
    s.print_square()
elif choice ==2:
    c = Circle()
    c.radius = float(input('Enter radius: '))
    c.print_circle()
elif choice ==3:
    t = Triangle()
    t.base = float(input('Enter base: '))
    t.high = float(input('Enter high: '))
    t.print_triangle()
else:
    print('Wrong choice!!!')