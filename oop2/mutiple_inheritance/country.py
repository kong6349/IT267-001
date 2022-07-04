from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    """def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.population = pop"""
        
        def __init__(self,name,area,pop) -> None:
            #super().__init__()   #ไม่ต้องมี self
            Geographic.__init__(self)
            Temperature.__init__(self)
            self.name = name
            self.area = area
            self.population = pop"

    def getpopulation(self):
        return self.population / self.area

    def showdetail(self):
        print(f'Country: {self.name}')

        print(f'Location: {self.getcordinate()}')
        print(f'Population: {self.population:,.2f}')
        print(f'Area: {self.area:,.2f}')
        print(f'Density: {self.getpopulation():,.2f}')

        print(f'Time Zone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperture(C): {self.getcelcius():,.2f}')
        print(f'Temperature(F): {self.getfahrenheit():,.2f}')
        print(f'Weather: {self.getweather()}')

        print('********************************')