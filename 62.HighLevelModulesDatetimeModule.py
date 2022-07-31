#Probably there aren't but it can be wrong
"""
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")

print(datetime.now())

right_now=datetime.now()

print(right_now.year)
print(right_now.month)
print(right_now.microsecond)

print(datetime.ctime(right_now))

print(datetime.strftime(right_now,"%Y %B"))

second=datetime.timestamp(right_now)
print(second)

right_now2=datetime.fromtimestamp(second)

print(right_now2)


history=datetime(2019,12,1)
right_now3=datetime.now()

difference=history-right_now3
print(difference)
"""











