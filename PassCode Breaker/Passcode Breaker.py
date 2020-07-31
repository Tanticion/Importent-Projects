
file = open('file.txt','r')
lst = []
for keys in file:
    lst.append(keys.replace('\n',''))

for key in lst:
    for i in range(1,11):
        if str(i) == key:
            print('key found: {}'.format(i))
            print(i)
            break


        for v in range(1,11):
            if str(i) + str(v)  == key:
                print('key found: {}{}'.format(i, v))
                print(i, v)
                break

            for x in range(1, 11):
                if str(i) + str(v)+ str(x) == key:
                    print('key found: {}{}{}'.format(i, v,x))
                    print(i, v, x)
                    break

                for m in range(1, 11):
                    if str(i) + str(v)+ str(x)+ str(m) == key:
                        print('key found: {}{}{}{}'.format(i, v,x,m))
                        print(i, v, x, m)
                        break

                    for n in range(1, 11):
                        if str(i) + str(v)+ str(x)+ str(m)+ str(n) == key:
                            print('key found: {}{}{}{}{}'.format(i, v,x,m,n))
                            print(i, v, x, m, n)
                            break


                        for o in range(1, 11):
                            if str(i) + str(v)+ str(x)+ str(m)+ str(n)+ str(o) == key:
                                print('key found: {}{}{}{}{}{}'.format(i, v,x,m,n,o))
                                print(i, v, x, m,n,o)
                                break

