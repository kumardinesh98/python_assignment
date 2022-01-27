'''
@author : Dinesh Kumar
@date : 24-01-2022
@last modified by : Dinesh Kumar
@last modified time : 25-01-2022
@title : two dimensional arrey
'''

from math import sqrt

def equation():
    a = 0
    b = 0
    c = 0
    while True:
        try :
            a = int(input("enter the value of a"))
            b =  int(input("enter the value of b"))
            c =  int(input("enter the value of c"))
            break
        except ValueError:
            print("enter a valid numbber")
    delta = (b*b)-4*a*c
    print(delta)
    root1 = (-(b) + sqrt(abs(delta)))/(2*a)
    root2 = (-(b) - sqrt(abs(delta)))/(2*a)
    print(root1)
    print(root2)


equation()