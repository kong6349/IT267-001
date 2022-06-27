from condo import Condo

ideo = Condo('Ideo',15,'fffewd',800,'condo')
ideo.show()

from project import Project

home = Project('Home',14,'Bang Yai')
home.show()
print(f'budget: {home.get_budget()} MB')
home.update_budget(30)
print(f'budget: {home.get_budget()} MB')