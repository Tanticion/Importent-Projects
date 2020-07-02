import re
compilc = re.compile(r'(\d+)+')
one = re.compile(r'\[, -(\d+\.0){1}\]')


class grat:


    def __init__(self,*args):
        self.data=args
        self.datalst = []
        self.datalsted = []
        self.lst = []
        self.datamist = []
        self.last =[]
        self.denta =[]


    def use(self):

        venv = compilc.findall(str(self.data))

        for value in range(10000,-10000,-1):

            self.lst.append(value)
        for i in venv:
            int(i)
            self.datalst.append(i)
            print('nanii',self.datalst)



        for i in range(1000,-1000,-1):
            if i ==0:
                continue
            for hi in self.datalst:
                if int(hi)/i in self.lst:
                    self.datalsted.append('({})x({})=({})'.format(i,int(hi)/int(i),int(hi)))
                    self.datamist.append(int(hi)/i)

                #print('number is :',int(self.data), '(/)', int(i) , '=', int(i))



                self.datalsted.sort()
                for ham in self.datalsted:

                    print('Factors: ', ham)
                    print(self.datalsted)
        if len(venv) !=1:

            for element in self.datamist:
                print(element)

                if self.datamist.count(element) >=len(self.data):

                    print('hdhdh: ',self.datamist.count(element))
                    print('CF: ',self.datamist)
                    print('No=umber of elemnts: ',len(venv))



                    self.denta.append(element)
               #    print(self.denta)
                    self.denta.sort()
                  #  print("GCF: ",self.denta[-1])





