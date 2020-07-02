import re


import math
class inpu:
    def __init__(self,val):
        self.input = val
        self.lst = []
        self.added = []

    def use(self):
        for i in self.input:
            val = int(i)*0.20

            self.lst.append(round(val))
        for i in self.lst:
            print('Profit: ',round(i))
        if len(self.input)>= 2:
            h=(sum(self.lst))
            print('Total profit: ',round(h))
            

result = inpu(input("insert the numbers: ").split(','))
result.use()
