'''
@author : Dinesh Kumar
@date : 24-01-2022
@last modified by : Dinesh Kumar
@last modified time : 25-01-2022
@title : two dimensional arrey
'''


class NegativeNumberError(Exception):
    pass


def array():
    exit = False
    while not exit:
        try:
            rows = int(input("enter number of rows"))
            columns = int(input("enter number of columns"))
            if rows <= 0 or columns <= 0:
                raise NegativeNumberError
            result = []
            for row in range(rows):
                temp = []
                for column in range(columns):
                    value = int(input(f"enter the value of {row},{column}"))
                    temp.append(value)
                result.append(temp)
            for item in result: print(item)
            exit = True
        except NegativeNumberError:
            print("please enter number graeter then zero")


array()
