from Inh import *   # * will import all the class present in Inh.py file
from BaseClass import *


class Derived(C1, C2, BaseClass):
    def emp(self, emp_name):
        super().empdetails("abc", 100) #This is a super method which run method of its super class
        print(f"Name of employee is {emp_name}")


en= Derived()
print(en.sum_num(10,12))
en.empdetails("kartik", 1000)
en.emp("Vicky")

print(en.greet('Boss', 'Pen'))
print(en.getConfig('Mysql', 'url'))

