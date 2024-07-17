#_------------------------------------_#
#             Date time
#_------------------------------------_#

import datetime

print(dir(datetime))#['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']      
print(dir(datetime.datetime))#['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__replace__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']

#print current date and time
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(dir(datetime.datetime.now()))

print(datetime.datetime.now().min)#0001-01-01 00:00:00
print(datetime.datetime.now().max)#9999-12-31 23:59:59.999999

#print current time
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)


print(datetime.time.min)#00:00:00
print(datetime.time.max)#23:59:59.999999
print(datetime.datetime(9999,12,31))
print(datetime.datetime(9999,12,31,12,00,55,1555))
birthday=datetime.datetime(2003,4,18)
date=datetime.datetime.now()

print(f"birthday : {birthday} and date now {date}")
print((date-birthday).days)

#----------------------------------#
#          Format Date             #
#----------------------------------#
#https://strftime.org/
#-----------------------------------

import datetime

print(date)
print(date.strftime("%a"))#Wed
print(date.strftime("%A"))#Wednesday
print(date.strftime("%b"))#Jul
print(date.strftime("%B"))#July
print(date.strftime("%d"))#17
print(date.strftime("%D"))#07/17/24
print(date.strftime("%d %B %Y"))#17 July 2024
print(date.strftime("%d-%B-%Y"))#17-July-2024
print(date.strftime("%d /%B /%Y"))#17 /July /2024



