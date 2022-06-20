class Coffee:
    def __init__(self,customer_name:str,menu:str,num:int = 1 , size:str = 'R',price:float,total:float = 0) -> None:
        self.customer = customer_name
        self.menu = menu
        self.num = num
        self.size = size
        self.price = price
        self.total = total
    
    def check_menu(self,Cafe_Mocha,Cappuccino,American,Cafe_Latte,Vanilla_Latte,Espresso):
        self.CM = Cafe_Mocha
        self.CP = Cappuccino
        self.AM = American
        self.CL = Cafe_Latte
        self.VL = Vanilla_Latte
        self.ES = Espresso

    def menu_dictionary(pri):
        pri = pri.check_menu()
        
    
    def computer_price(ch):
        ch = ch.upper()
        if ch == 'L':
            return 'บวกเพิ่ม $1 '
        elif ch == 'XL':
            return 'บวกเพิ่ม $1.5 '
    
    def display_detail(self):
        print(f'customer_name: {self.customer}')
        print(f'menu: {self.menu}')
        print(f'size: {self.size}')
        print(f'num: {self.num}')
        print(f'price: {self.price}')
        print(f'total: {self.total}')



