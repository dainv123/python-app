import time

from calendar import monthrange, isleap


# this function to convert a valid number to number of month
def convert_age_to_months(age):
    localtime = time.localtime(time.time())

    try:
        if isinstance(age, bool): 
            raise

        year = int(age)
        
    except Exception:
        raise ValueError('Not a valid age')
    

    month = year * 12 + localtime.tm_mon

    return month


# this function to convert a valid number to number of day
def convert_age_to_days(age):
    day = 0
    
    try:
        if isinstance(age, bool): 
            raise

        year = int(age)
        
    except Exception:
        raise ValueError('Not a valid age')

    localtime = time.localtime(time.time())

    begin_year = int(localtime.tm_year) - year

    end_year = begin_year + year

    # calculate the days in begin_year > end_year
    for y in range(begin_year, end_year):
        if (isleap(y)):
            day = day + 366
        else:
            day = day + 365
    
    # calculate the days in end_year from 1 > current month
    for m in range(1, localtime.tm_mon):
        day = day + monthrange(localtime.tm_year, m)[1]

    # calculate the days in current month
    day = day + localtime.tm_mday

    return day

def main():
    while True:
        age = input('Please enter your age: ')
        try:
            days = convert_age_to_days(age)
            months = convert_age_to_months(age)

        except ValueError:
            print ('Valid number, please')
            continue

        print ("Your age: %s, It's similar to %s months or %s days" % (age, months, days))
        break
    
    
if __name__ == "__main__":
    main()