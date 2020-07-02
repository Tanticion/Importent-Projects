class func :
    def __init__(self):
        self.lst = [1,1]
    def funci(self):
        i = 0
        vol = 0
        v = 1
        while vol<100028:
            vol+=1
            val = self.lst[i] + self.lst[v]
            self.lst.append(val)
            i += 1
            v += 1

            print("iteration number",i,"number",val)


        # for i in self.lst:
        #     if self.lst.count(i) >=2:
        #         self.lst.remove(i)


func().funci()
