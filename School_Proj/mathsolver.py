import Collatz
import one
import twonums
import drag
import infinite
import biology

def func88(which):
    if which == str(1):
        num1 = int(input('insert the first number: '))
        one.grat(num1).use()
    elif which == str(2):
        num1 = int(input('insert the first number: '))
        num2 = int(input('insert the second number: '))
        Collatz.grat(num1,num2).use()

    elif which == str(3):
        num1 = int(input('insert the first number: '))
        num2 = int(input('insert the second number '))
        num3 = int(input('insert the third number '))
        drag.grat(num1,num2,num3).use()

    elif which == str(4):
        num1 = int(input('insert the first number: '))
        num2 = int(input('insert the number to reach '))
        twonums.grat(num1,num2).use()
    elif which == str(5):
        num1 = input('insert an infinite amount of numbers: ')
        infinite.grat(num1).use()

    elif which == str(6):
            subject = str(input('Choose a subject\n1:equations\n2:others\n3:science\n4:vocabulary\n5:search all directories\nnumber:'))
            num1 = input('insert a question: ')

            biology.show(num1).result(subject)


    else:
        print('WRONG NUMBER ENTERED')

func88(input('''1:FIND COMMON FACTORS OF ONE NUMBERS\n2:FIND FACTORS OF TWO NUMBERS\n3:FIND THE COMMON FACTOR OF THREE NUMBERS\n4:FIND TWO NUMBERS THAT MULTIPLY TO A NUMBER AND ADD TO A SECOND NUMBER\n5:FIND A COMMON FACTOR OF AN INFINATE AMOUNT OF NUMBERS\n6:ANSWRS DATABASE\nINSERT A NUMBER: '''))
