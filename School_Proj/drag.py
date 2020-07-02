
class grat:

    def __init__(self,args,kwargs,dwargs):
        self.data=args
        self.data2=kwargs
        self.data3 = dwargs
        self.lst = []
        self.datalst = []
        self.data2list = []
        self.data3list = []



    def use(self):

        for value in range(10000,-10000,-1):


            self.lst.append(value)



        for i in range(1000,-1000,-1):
            if i == 0:
                continue
            if self.data/i in self.lst:
                self.datalst.append(i)

                print('number is ',self.data, '/', i , '=', self.data/i)
                print('data', self.datalst)


        for i in range(1000,-1000,-1):
            if i == 0:
                continue

            if self.data2/i in self.lst:
                self.data2list.append(i)

                print('number is ', self.data2, '/', i, '=', self.data2/i)
                print('data', self.data2list)
                self.datalst.sort()




        for i in range(1000,-1000,-1):
            if i == 0:
                continue

            if self.data3/i in self.lst:
                self.data3list.append(i)

                print('number is ', self.data3, '/', i, '=', self.data3/i)
                print('data', self.data3list)
        for result in self.datalst :
            if result in self.data2list and result in self.data3list:
                print('CF: ',result)


    def retdata(self):
        data = self.datalst
        return data

