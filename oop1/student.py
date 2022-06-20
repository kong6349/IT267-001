class Student:
    def __init__(self,id:str,name:str,major:str = "IT") -> None:
        self.id = id
        self.name = name
        self.major = major
    
    def display_detail(self):
        print(f'Id: {self.id}')
        print(f'Name: {self.name}')
        print(f'Major: {self.major}')
    
    def __del__(self):
        print("object has destroy")

if __name__=="__main__":
    jessa = Student('dex','Jessa','room')
    jessa.display_detail()
    amy = Student('113','Amy')

    amy.display_detail()