import calendar
from datetime import date
m, d, y = map(int, input().split())
day=(calendar.day_name[calendar.datetime.date(y, m, d).weekday()]).upper()
print(day)
