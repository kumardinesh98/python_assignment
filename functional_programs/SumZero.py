'''
@author : Dinesh Kumar
@date : 24-01-2022
@last modified by : Dinesh Kumar
@last modified time : 25-01-2022
@title : two dimensional arrey
'''


def get_value():
    values = []
    while True:
        try:
            total = int(input("enter total count :"))
            break
        except ValueError:
            print("please enter a valid number")
    for count in range(int(total)):
        while True:
            try:
                temp = int(input(f"enter {count} number"))
                values.append(temp)
                break
            except ValueError:
                print("please enter a valid number")

    return values


def find_sum():
    values = get_value()
    length = len(values)
    for i in range(length - 2):
        for j in range(i+1, length - 1):
            for k in range(j+1, length):
                if (values[i] + values[j] + values[k]) == 0:
                    print(values[i],values[j],values[k])


find_sum()