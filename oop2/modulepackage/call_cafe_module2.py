import cafe
dessert_menu = cafe.Dessert()
print(dessert_menu.show_dessert())

drink_menu = cafe.Drink()
print(drink_menu.show_drink())

drink_menu.add_drink('juice')
drink_menu.add_drink('smoothy')
print(drink_menu.show_drink())