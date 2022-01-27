def find_leapyear(year):
    if year < 1000 or year > 9999:
        return "please enter a valid year"

    if(year % 400 == 0)|((year % 100 != 0) & (year % 4 == 0)):
        return "leap year"

    return "not a leap year"

find = int(input("enter year"))
print(find_leapyear(find))