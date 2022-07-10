from horse import Horse
class Donkey(Horse):
    def __init__(self, max_height: float, name: str, color: str, age: int , weight: float) -> None:
        super().__init__(max_height, name, color)
        self.age = age
        self.weight = weight

    def sound(self):
        print(f'Donkey make eeyore sound')

    def show_info(self):
        super().show_info()
        print(f'Age: {self.age}-year-old')
        print(f'Weight: {self.weight} kg')