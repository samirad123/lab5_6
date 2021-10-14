import datetime
from datetime import time
#module.class.function
current_date_time = datetime.datetime.now()
print(current_date_time)

#OOP
#class - >functions
#object = Label(root)

#display date
current_date = datetime.date.today()
print(current_date)

#to display the date values
user_date = 4
user_month = 7
user_year = 2021

user_date_display = datetime.date(user_year,user_month,user_date)
print(user_date_display)

#to display the date,year,month values seperately
today_date = datetime.date.today()
print("Current year",today_date.year)
print(today_date.month)
print(today_date.day)

#time
#hour minutes seconds
#hour = 0 ,min = 0,sec =0 (initialised value)
date_time = datetime.time()
print(date_time)
#dt=datetime.time(hours,min,sec)
dt = datetime.time(10,18,40)
print(dt)

t2 = datetime.time(hour = 10,minute = 20,second = 22)
print(t2)

#to pass microsecond value
t3= datetime.time(10,21,59,345677)
print(t3)

#seperate hrs,min,sec
t4 = datetime.time(10,18,40)
print(t4.hour)
print(t4.minute)
print(t4.second)
print(t4.microsecond)

#diff between dates
date1 = datetime.date(2021,9,28)
date2 = datetime.date(1800,8,27)
date_diff = date1 - date2
print(date_diff)

#diff between dates and time
date3 = datetime.datetime(2021,9,28,10,30,40)
date4 = datetime.datetime(1800,8,27,9,29,30)
datetime_diff = date3 - date4
print(datetime_diff)



