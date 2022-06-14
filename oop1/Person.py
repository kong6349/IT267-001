from unicodedata import name


class Person:
    country = "Thailand"
    def __init__(self,name,gender,profession,study) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study

    def work(self):
        print(f'{self.name} is working as a {self.profession}')
    def studie(self):
        print(f'{self.name} studies for {self.study} hour(s)') 
    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} study: {self.study} ')

jessa = Person("Jessa","Male","Software Engineer",10)
jessa.show()
jessa.work()
jessa.studie()

jon = Person("Jon","Male","Doctor",15)
jon.show()
jon.work()
jon.studie()

lalisa = Person("Lalisa","Female","Korean Singer",13)
lalisa.work()

print(f"Class Variable: {Person.country}")
print(f"Intance Variable: {lalisa.country}")

#assign value
lalisa.country = "Korea"
print("__________")
print(f"Class Variable: {Person.country}")
print(f"Intance Variable: {lalisa.country}")
print(f"Intance Variable: {jon.country}")

Person.country ="England"
print("__________")
print(f"Class Variable: {Person.country}")
print(f"Intance Variable: {lalisa.country}")
print(f"Intance Variable: {jon.country}")