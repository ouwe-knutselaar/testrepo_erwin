from datetime import datetime
from datetime import time

class Employee:

    """Dit is echt een baggerclass"""

    __minimal_salary=12000

    def __init__(self,naam,salaris):
        self.__naam=naam
        self.__salaris=Employee.__minimal_salary if salaris<Employee.__minimal_salary else salaris
        self.__start_datum=datetime.now()

    def PayRaise(self,extra):
        self.__salaris += extra

    def __str__(self):
        return str("%s %.2f %s"%(self.__naam,self.__salaris,self.__start_datum.strftime("%c")))

    def getName(self):
        return self.__naam

    def getSalary(self):
        return self.__salaris

    def getStartDate(self):
        return self.__start_datum

    def payBonus(self,percentage=1,min=__minimal_salary,max=9999999999):
        temp=(self.__salaris/100)*(100+percentage)
        print(min)
        if temp>max:temp=max
        if temp<min:temp=min
        self.__salaris=temp

    def __eq__(self,other):
        return self.__naam == other.__naam and self.__salaris == other.__salaris

    def __ne__(self, other):
        return self.__naam != other.__naam or self.__salaris != other.__salaris

    def __lt__(self, other):
        return self.__salaris < other.__salaris

    def __gt__(self, other):
        return self.__salaris > other.__salaris

    @staticmethod
    def dump():
        print("doe iets")




