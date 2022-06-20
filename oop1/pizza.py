class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'
@classmethod
def margherita(cls):
    return cls (['mozzarella','tomatoes'])
@classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
   
@staticmethod
    def size(ch):
        ch = ch.upper()
        if ch == 'S':
            return 'small: 6 inches, 4 slices'
        elif ch == 'L':
            return 'Large: 14 inches, 10 slices'
        else:
            return 'Default Medium: 12 inches, 8 slices'
        my_pizza = Pizza('Cheese, Meat')

print(my_pizza)
print(my_pizza.margherita())

print('---- Static Method ----')
print(Pizza.size('L'))

print('---- Class Method ----')
print(Pizza.margherita())
print(Pizza.prosciutto())
print(my_pizza.margherita())
print(Pizza.ingredients)
