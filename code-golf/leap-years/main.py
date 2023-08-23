""" 
In the Gregorian calendar, a leap year is created by extending February to 29 days in order to keep the calendar year synchronized with the astronomical year. These longer years occur in years which are multiples of 4, with the exception of centennial years that aren’t multiples of 400.

 """

for y in range(1800, 2401):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            exit
        else:
            print(y)
