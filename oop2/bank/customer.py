class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.address = ''
        self.phone = ''

    def new_customer(self):
        self.name = input('Enter costomer name: ')
        self.address = input('Enter costomer address: ')
        self.phone = input('Enter costomer phone: ')

    def cus_info(self):
        return (f'name: {self.name}\naddress: {self.address}\nphone: {self.phone}')

