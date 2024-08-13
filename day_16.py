# python datetime similar to r lubridate
import day_6
from datetime import timedelta
from datetime import datetime
from datetime import time
from datetime import date
print(dir(datetime))
# prints all functions and methods in the datetime library

now = datetime.now()
print(now)  # 2024-08-12 13:30:06.955937
now.hour  # 13

year_0 = datetime(2000, 1, 1)
print(year_0)  # 2000-01-01 00:00:00

# Formatting Date Output Using
diff_format = year_0.strftime("%d, %m, %Y")
print(diff_format)

# format string to date:
date_str = '2024, Monday, 5'  # just chooses first day of the month
dates = datetime.strptime(date_str, "%Y, %A, %m")
print(dates)

t = time(10, 10, 20)
print(t)  # 10:10:20

# difference in time
today = date(year=2024, month=8, day=12)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

# using timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)


# exercises:
rand = day_6.create_randint(1, 6, 3)
print(rand)

# 1 : Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.now()
# print(now) # 2024-08-13 12:28:49.616908


# 3 Today is 5 December, 2019. Change this time string to time.
a_date = '5, December 2019'
a_date = datetime.strptime(a_date, '%d, %B %Y')
# print(a_date)  # 2019-12-05 00:00:00


# 6
'''Think, what can you use the datetime module for? Examples:
Time series analysis
To get a timestamp of any activities in an application
Adding posts on a blog'''

'''Answer: time stamps to track uses of certain websites, i.e. when accessed'''
