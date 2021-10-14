import time

simple_format=time.strftime("%a, %d %b %Y %H:%M:%S + 1010",time.gmtime())
print(f"\nSimple format of time :\n{simple_format}")

full_format=time.strftime("%A, %D %B %Y %H:%M:%S + 0000",time.gmtime())
print(f"\nFull names and representation :\n{full_format}")

preferred_format=time.strftime("%x, %X")
print(f"\nPreferred format :\n{preferred_format}\n\n")























import datetime
print("Current date and time",datetime.datetime.now())
print("Current year :  ",datetime.date.today().strftime("%Y"))
print("Month of year :  ",datetime.date.today().strftime("%B"))     #string value
print("Month of year :  ",datetime.date.today().strftime("%m"))     #numerical value
print("Week number of the year :  ",datetime.date.today().strftime("%W"))
print("Weekday of the week :  ",datetime.date.today().strftime("%w"))   #Numerical Value
print("Day of year :  ",datetime.date.today().strftime("%j"))
print("Day of the month :  ",datetime.date.today().strftime("%d"))
print("Day of week :  ",datetime.date.today().strftime("%A"))       #String Value


#import datetime

#print("c_date_time :",datetime.datetime.now())
#print("c_year :",datetime.date.today().strftime("%Y"))
#print("month_year :",datetime.date.today().strftime("%m"))
#print("week_num :",datetime.date.today().strftime("%W"))
#print("weekday_week",datetime.date.today().strftime("%w"))
#print("day_year",datetime.date.today().strftime("%j"))
#print("day_week",datetime.date.today().strftime("%A"))
#print("date_of_month",datetime.date.today().strftime("%d"))

#%B for writing name of month
