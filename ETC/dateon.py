# import datetime
from datetime import *

import time
current = datetime.datetime.now()

print(current)
tomorrow = current + datetime.timedelta(days=1)
print(tomorrow)


# def stand_by_time(TraketTime):
#     now = datetime.now()
#     nowDate = now.strftime('%Y-%m-%d')
#     # TraketTime = '09:00:01'
#     # TraketTime = '16:24:25'
#     dt_want = nowDate + ' ' + TraketTime
#     print(dt_want)

# want_time = datetime.strptime(dt_want, '%Y-%m-%d %H:%M:%S')
# while datetime.now() < want_time:
#     print(datetime.now().strftime('%H:%M:%S'))
#     # print('stand_by')
#     time.sleep(1)
# stand_by_time("11:55:00")
