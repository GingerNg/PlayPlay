# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@word: datacollection_job.py
@time: 2018/5/4 18:05
"""
import datetime
import time

import pytz

from utils.constants import TimeUnit

def time2CCT_timestamp(date_time):
    # 转换成时间戳
    """
    CCT / UTC date_time 2 CCT_timestamp
    2018-08-12 09:36:06.009219+00:00
    2018-08-13T13:24:03+0800
    """
    # cct = True
    if date_time.endswith("+0800"):
        cct = False
    if date_time == "":
        return ""
    if len(date_time) >= 19:
        date_time = date_time[0:18]
    date_time = date_time.replace(" ","T")
    timeArray = time.strptime(date_time, "%Y-%m-%dT%H:%M:%S")
    # if cct:
    #     timeArray = timeArray - datetime.timedelta(hours=8)
    timestamp = time.mktime(timeArray)
    return str(timestamp*10)[0:10]

def CCT_timestamp2CCT_datetime(timestamp):
    """
    1534137843 -->  2018-08-13T13:24:03+0800
    :param timestamp:
    :return:
    """
    if timestamp == "":
        return ""
    timeStamp = int(timestamp)
    dateArray = datetime.datetime.fromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime('%Y-%m-%dT%H:%M:%S+0800')
    return otherStyleTime  # 2013--10--10 15:40:00

def getdatetime():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def today_now():
    return str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))

def yesterday_now():
    return str((datetime.datetime.now()+ datetime.timedelta(days = -1)).strftime('%Y-%m-%dT%H:%M:%S'))

def getdatetimefloat():
    return time.time() # float


def getdatetimedouble():
    return int(round(time.time() * 1000))


def is_late(start_time, now=datetime.datetime.now()):
    now = now.replace(tzinfo=pytz.timezone('UTC'))
    if start_time > now:
        return False
    else:
        return True


def plus_time(start_time, interval_time):
    try:
        interval = int(interval_time.strip(TimeUnit.days.name).\
                                strip(TimeUnit.hours.name).\
                                strip(TimeUnit.mins.name).\
                                strip(TimeUnit.secs.name))
        if interval_time.endswith(TimeUnit.days.name):
            return start_time + datetime.timedelta(days=interval)
        elif interval_time.endswith(TimeUnit.hours.name):
            return start_time + datetime.timedelta(hours=interval)
        elif interval_time.endswith(TimeUnit.mins.name):
            return start_time + datetime.timedelta(minutes=interval)
        elif interval_time.endswith(TimeUnit.secs.name):
            return start_time + datetime.timedelta(seconds=interval)
    except Exception as e:
        print(e)


def plus_time_util_late(start_time, interval_time, now=datetime.datetime.now()):
    while is_late(start_time, now):
        start_time = plus_time(start_time, interval_time)
    return start_time


def timestamp_to_str(time_stamp):
    time_array = time.localtime(time_stamp)
    time_str = time.strftime("%Y-%m-%d %H:%M", time_array)
    return time_str


if __name__ == "__main__":
    # print(getdatetimedouble())
    # print(type(getdatetimedouble()))

    # pre = datetime.datetime.now()
    # time.sleep(1)
    # now = datetime.datetime.now()

    now = time.time()
    print(now)
    print(int(now))
    # print(is_late(pre,now))

    # print (plus_time(now,"1mins"))
    #
    print(time2CCT_timestamp("2018-10-10T00:00:00"))
    #
    # print(len("2018-09-05 22:26"))

    print(getdatetime())

