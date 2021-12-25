import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

# this function to convert a valid number to number of month
def convert_age_to_months(age):
  if type(age) == bool: 
    return 'Not a valid age'

  localtime = time.localtime(time.time())

  year = int(age)

  month = year * 12 + localtime.tm_mon

  return month


# this function to convert a valid number to number of day
def convert_age_to_days(age):
  # check bool
  if type(age) == bool: 
    return 'Not a valid age'

  day = 0
  
  year = int(age)

  localtime = time.localtime(time.time())

  begin_year = int(localtime.tm_year) - year

  end_year = begin_year + year

  # calculate the days in begin_year > end_year
  for y in range(begin_year, end_year):
      if (judge_leap_year(y)):
          day = day + 366
      else:
          day = day + 365

  leap_year = judge_leap_year(localtime.tm_year)
  
  # calculate the days in end_year from 1 > current month
  for m in range(1, localtime.tm_mon):
      day = day + month_days(m, leap_year)

  # calculate the days in current month
  day = day + localtime.tm_mday

  return day