import re
positive = re.compile(r'\'(\d)+(x)(\d)+.0(=)(\d)+')
negitive = re.compile(r'-(\d)+(x)-(\d)+.0(=)(\d)+|-(\d)+(x)(\d)+.0(=)-(\d)+|-(\d)+(x)(\d)+.0(=)-(\d)+|\'(\d)*(x)-(\d)+.0(=)-(\d)+\'')
commas = re.compile(r'(\(\'\',)*')

class grat:

    def __init__(self,args):
        self.data=args
        self.datalst = []
        self.lst = []

    def use(self):

        for value in range(10000,-10000,-1):

            self.lst.append(value)



        for i in range(1000,-1000,-1):
            if i ==0:
                continue
            if self.data/i in self.lst:
                self.datalst.append('({})x({})=({})'.format(i,int(self.data)/int(i),int(self.data)))

                #print('number is :',int(self.data), '(/)', int(i) , '=', int(i))

                print('First 5 factors: ', self.datalst[1:5])

                for self.ham in self.datalst:

                    print('Factors: ', self.ham)
