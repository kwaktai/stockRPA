from datetime import datetime
import time


def stand_by_time(TraketTime):
    now = datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    dt_want = nowDate + ' ' + TraketTime
    want_time = datetime.strptime(dt_want, '%Y-%m-%d %H:%M:%S')
    while datetime.now() < want_time:
        print(datetime.now().strftime('%H:%M:%S'))
        # print('stand_by')
        time.sleep(1)

# 만약 22:00 ~ +1day 이면

# if 06 ~ 21 이면 "res"
# else 22 ~ 05 "basic"
# if 09


def findBuyingtime():
    now = datetime.now()
    nowHour = int(now.strftime('%H'))
    nowMin = int(now.strftime('%M'))
    if 6 <= nowHour < 22:
        if nowHour == 21 and nowMin > 53:
            TraketTime = ("22:00:00")
            nowDate = now.strftime('%Y-%m-%d')
            dt_want = nowDate + ' ' + TraketTime
            want_time = datetime.strptime(dt_want, '%Y-%m-%d %H:%M:%S')
            while datetime.now() < want_time:
                print(datetime.now().strftime('%H:%M:%S'))
        # print('stand_by')
                time.sleep(1)
        return "res"
    else:
        return "basic"


# print(findBuyingtime())
