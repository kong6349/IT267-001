from pydoc import text


class Car:
    def __init__(self,model,colour,year,price) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    def print_detail(self):
        print(f'Model: {self.model}')
        print(f'Colour: {self.colour}')
        print(f'Year: {self.year}')
        print(f'Price: {self.price}')

    #static method ไม่ต้องมี self
    @staticmethod
    def get_static_method(text):
        print(f'String: {text}')
    @classmethod
    def get_class_method(cls,text):
        print(f'This is class method with {text}')

if __name__=="__main__":
    my_car = Car('Cross','White',2022,1500000)
    my_car.print_detail()
    Car.get_static_method('Hello Class')
    my_car.get_static_method('Good Car Object')
    Car.get_class_method('Go home')