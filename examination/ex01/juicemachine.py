class JuiceOrder:
    def __init__(self,menu:str,size:str,price:int) -> None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.price = price

    def check_menu(self):
        menu = {'OJ': 25,
                'AJ': 25,
                'WJ': 30,
                'PJ': 30}

    def compute_price(self):
        if self.size =='R':
            self.price += 0
        elif self.size == 'L':
            self.price += 5
        else:
            self.price
        JuiceOrder.total = self.price

    def display_order(self):
        self.check_menu()
        self.compute_price()
        return(f'{self.menu} ({self.size} * {self.price}) => {JuiceOrder.total}')


if __name__ == "__main__":
    order1 = JuiceOrder('wj','l',30)
    print(order1.display_order())
    order2 = JuiceOrder('oj','r',25)
    print(order2.display_order()) 
    order3 = JuiceOrder('pj','l',30)
    print(order3.display_order()) 