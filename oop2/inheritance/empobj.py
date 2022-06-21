from empit import Empit
from empmkt import EmpMKT

mike = Empit('001','Mike',60000)
mike.add_skill('Python,Javasrcipt')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()


anna = EmpMKT('002','Anna',35000)
anna.emp_detail()
anna.mkt_salary()

paul = EmpMKT('003','Paul',45000)
paul.add_commision(35)
paul.add_location('Chiang Mai')
paul.emp_detail()
paul.mkt_salary()