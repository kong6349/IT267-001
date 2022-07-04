from animal import Animal

class Dog(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print(f'I am a dog.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} year old')

    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Woof!! sound')

class Cat(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print(f'I am a cat.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} year old')

    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Meaw!! sound')

class Cow(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print(f'I am a cow.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} year old')

    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Moo!! sound')
