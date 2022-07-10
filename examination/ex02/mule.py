from donkey import Donkey
class Mule(Donkey):

    def __init__(self, max_height: float, name: str, color: str, age: int, weight: float) -> None:
        super().__init__(max_height, name, color, age, weight)

    def run(self):
        print(f'Mule is running')

    def show_info(self):
        super().show_info()
        print('-------------------')

mule1 = Mule(200,'Mumu','Blue-eye Cream',3,200)
mule1.show_info()

mule2 = Mule(200,'Meme','Palomino',1,120.7)
mule2.sound()
mule2.show_info()