
class grat:

    def __init__(self,args,kwargs='whatever'):
        self.data=args
        self.data2=kwargs
        self.lst = []
        self.datalst = []
        self.data2list = []

    def use(self):

        for value in range(1000,-1000,-1):


            self.lst.append(value)



        for i in range(1000,-1000,-1):
            if i == 0:
                continue
            if self.data/i in self.lst :
                self.datalst.append(i)

                #print('number is ',self.data, '/', i , '=', self.data/i)
                #print('data', self.datalst)

                #print('common factor: ',self.datalst[-1])
               # self.datalst.sort()
               # print('greates value: ',self.datalst[-1])

            if self.data/i + i ==self.data2:
                 print('common number: ', int(self.data/i), '(+)', i, '=', self.data2)
            #if self.data/i - i ==self.data2:
             #    print('common number: ', int(self.data/i), '(-)', i, '=', self.data2)
      




