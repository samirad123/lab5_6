from datetime import datetime
current_Timestamp = datetime.now()
print(current_Timestamp)

# method used = strftime = formatted string(string format time)

#%Y - year (4 digit value)
#%m - month
#%d - day
#%H - hour
#%M - minutes
#%S - second

current_Time = current_Timestamp.strftime("%H:%M:%S")
print(current_Time)

current_date = current_Timestamp.strftime("%d/%m/%Y")
print(current_date)
