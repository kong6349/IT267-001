from unicodedata import name


class Animal:
    animal = "cat"

    def new_animal(self,name:str,breed:str,colour:str,age:int):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age

    def print_detail(self):
        print("---------------------")
        print(f'Name: {self.name}')
        print(f'Animal: {self.animal}')
        print(f'Breed: {self.breed}')
        print(f'Colour: {self.colour}')
        print(f'Age: {self.age}')
    
    def __del__(self):
        print(f"Object was destroy")

#create object
if __name__=="__main__":
    Animal.animal = "fish"
    ula = Animal()
    ula.new_animal("Ula","Scottish","White",1)
    ula.animal = "Dog"
    ula.print_detail()

    drac = Animal()
    drac.new_animal("Drac","Scottish","White",1)
    drac.print_detail()
    drac.breed = "catfish"
    drac.print_detail()

    #เรียกดูข้อมูลของ object ผ่านทางชื่อ Class
    Animal.print_detail(ula)
    Animal.print_detail(drac)

    #เรียก class varibale ทั้งหมด
    print(f'{Animal.__dict__}')
    
    print(f'{ula.__dict__}')


    peter = Animal()
    peter.new_animal("Peter","Parrot","green yellow red",2)

    peter.legs = 2
    print(f'{peter.__dict__}')