
date = input('Enter date as mm/dd/yyyy: ')

month = int(date[:2])
day = int(date[3:5])
year = int(date[6:])

if month == 1:
    print(f'January {day}, {year}')
if month == 2:
    print(f'February {day}, {year}')
if month == 3:
    print(f'March {day}, {year}')
if month == 4:
    print(f'April {day}, {year}')
if month == 5:
    print(f'May {day}, {year}')
if month == 6:
    print(f'June {day}, {year}')
if month == 7:
    print(f'July {day}, {year}')
if month == 8:
    print(f'August {day}, {year}')
if month == 9:
    print(f'September {day}, {year}')
if month == 10:
    print(f'October {day}, {year}')
if month == 11:
    print(f'November {day}, {year}')
if month == 12:
    print(f'December {day}, {year}')


def dayfinder(date):
    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:])
    if month == 1:
        daydate = day
    if month == 2:
        daydate = (day+31)
    if month == 3:
        daydate = (day+59)
    if month == 4:
        daydate = (day+90)
    if month == 5:
        daydate = (day+120)
    if month == 6:
        daydate = (day+151)
    if month == 7:
        daydate = (day+181)
    if month == 8:
        daydate = (day+212)
    if month == 9:
        daydate = (day+243)
    if month == 10:
        daydate = (day+273)
    if month == 11:
        daydate = (day+304)
    if month == 12:
        daydate = (day+334)


    
    daydate = (daydate + ((year-1)*365))
    daydate = (daydate + (year//4))
    daydate = (daydate - (year//100))
    daydate = (daydate + (year//400))
    if year%4 == 0 and month >= 2:
        daydate -= 1


    daydate = daydate%7

    if daydate == 1:
        day_of_week = 'Monday'
    if daydate == 2:
        day_of_week = 'Tuesday'
    if daydate == 3:
        day_of_week = 'Wednesday'
    if daydate == 4:
        day_of_week = 'Thursday'
    if daydate == 5:
        day_of_week = 'Friday'
    if daydate == 6:
        day_of_week = 'Saturday'
    if daydate == 0:
        day_of_week = 'Sunday'
    

    return day_of_week

print(dayfinder(date))


    

    

    












