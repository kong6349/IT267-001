class Rectangle:
    def __init__(self,width,length) -> None:
        self.width = width
        self.length = length
        self.area = 0
    def get_data(self):
        pass
    def computer_area(self):
        self.area = self.width * self.length
    def print_area(self):
        print(f"Rectangle Area : {self.area}")

rec_obj = Rectangle(4.5,8)
rec_obj.computer_area()
rec_obj.print_area()