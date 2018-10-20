import time
print(time.localtime())  #这样就可以print 当地时间了
""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=12, tm_sec=48, tm_wday=4, tm_yday=358, tm_isdst=0)
"""

import time as t
print(t.localtime()) # 需要加t.前缀来引出功能

""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=12, tm_sec=48, tm_wday=4, tm_yday=358, tm_isdst=0)
"""

from time import time, localtime
print(localtime())
print(time())
""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=41, tm_sec=38, tm_wday=4, tm_yday=358, tm_isdst=0)

1482475298.709855
"""

from time import *
print(localtime())
""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=41, tm_sec=38, tm_wday=4, tm_yday=358, tm_isdst=0)
"""

