bird_type = 'parrot'

class Bird:
    bird_name = 'Peter'

    def __init__(self,color) -> None:
        self.color = color
        country = 'Thailand'

        print(country)

    def show(self):
        return(f'{bird_type}{Bird.bird_name} has {self.color}')
    
if __name__=='__main__':
    print(f'********{bird_type}*********')
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())

    print(Bird.bird_name)
    print(my_bird.bird_name)

    print(my_bird.color)