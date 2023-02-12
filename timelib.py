import time

a = time.gmtime()
a
b = time.localtime()
b

time.ctime()
time.asctime()
time.ctime(1000000000)


from datetime import datetime
from datetime import date, time
import datetime

datetime.now()

datetime(2021, 3, 21, 11, 15)

date(2021, 3, 21)
time(20,41,44)

datetime.fromtimestamp(1000000000)

datetime.now().timetuple()

datetime.now().isoformat()

t1 = datetime(2021,4,1,18,30,0)
t2 = datetime(2021,4,1,23,0,0)

str((t2-t1)*5)

d = datetime.timedelta(hours=4, seconds=1800)
str(d)

short_class = datetime.timedelta(days=4.5)
long_class = datetime.timedelta(days=4)
short_class < long_class

str(long_class)

str(long_class.total_seconds())


import arrow

t = arrow.utcnow()
t.year
t.month

ny = t.to('America/New_York')
lc = arrow.now('local')

s = '2023-02-12 14:36'
s.format('HH:mm ss ZZZ')
arrow.get(s)

t = arrow.get(1_000_000)
t.humanize()

import datetime

lc - arrow.get(s)

start = arrow.utcnow()
end = arrow.utcnow() + datetime.timedelta(hours=6)

for one_minute in arrow.Arrow.span_range('hour', start, end):
    print(one_minute)
