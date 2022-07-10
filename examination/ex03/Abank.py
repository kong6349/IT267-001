from multiprocessing import Value
from interface import Interface
class ABank(Interface):
    def __init__(self, bankname: str, loanamount:int ,loanyear:int, loanrate:float, interest:float, monthlypay:float) -> None:
        super().__init__(bankname)
        self.__loanamount = loanamount
        self.__loanyear = loanyear
        self.__loanrate = loanrate
        self.interest = interest
        self.monthlypay = monthlypay

    @property
    def loanamount(self):
        return self.__loanamount
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value

    @property
    def loanyear(self):
        return self.__loanyear
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value

    @property
    def loanrate(self):
        return self.__loanrate
    @loanrate.setter
    def loanrate(self,value):
        self.__loanrate = value

    def flat_rate(self):
        self.interest = (f'{self.loanamount * self.loanrate / self.loanyear} ')
        self.monthlypay = (f'{self.loanamount + self.interest/24}')
        

    def display_interest(self):
        print(f'*******{self.bankname} Loan Info********')
        print(f'Loan: {self.loanamount:,.2f}')
        print(f'Rate: {self.loanrate:,.2f} %')
        print(f'Year: {self.loanyear}')
        print(f'-- interest--')
        print(f'Interest: {self.interest:,.2f} baht')
        print(f'Monthly Repayment: {self.monthlypay:,.2f} baht')
        

scb = ABank('SCB',100000,2,3,6000,4416.67)
scb.display_interest()