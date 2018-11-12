# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: constants.py
@time: 2018/4/16 10:18
"""

from enum import Enum

class CleanStatus(Enum):
    """
    http请求返回状态
    """
    succeed = "成功"
    failed = "失败"
    exception = "异常"

class CleanCode(Enum):
    """
    http请求返回状态
    """
    succeed = "成功"
    no_pub_time = "pub_time 不存在"  # pub_time 不存在
    parse_pub_time = "pub_time 解析失败"   # pub_time 解析失败
    other = "其他错误"

class TimeUnit(Enum):
    """
    时间单位
    """
    secs = "秒"
    mins = '分'
    hours = '时'
    days = '天'

class TaskStatus(Enum):
    """
    任务运行状态
    """
    new = "新建"
    running = "运行"
    succeed = "成功"
    failed = "失败"


class ScriptStatus(Enum):
    """
    脚本状态
    """
    new = "新建"
    running = "运行"
    stop = "成功"
    paused = "失败"


class TaskType(Enum):
    """
    任务type
    """
    sync = "新建"
    async = "运行"


class PluginStatus(Enum):
    """
    plugin状态
    """
    check = "新建"
    online = "运行"
    offline = "运行"


class JobStatus(Enum):
    """
    任务运行状态
    """
    new = "新建"
    running = "运行"
    submitted = "task全部"
    finished = "完成"
    checking = "检查"



class HttpResponseStatus(Enum):
    """
    http请求返回状态
    """
    succeed = "0"
    failed = "1"


ROOT_DATA_PATH = "/home/ginger/data"

CONF_PATH = ""
INPUT = "input"
OUTPUT = "output"

node_name = "node1"


if __name__ == "__main__":
    # f = JobStatus("失败")
    # print (JobStatus.failed.value)
    # print (JobStatus.failed.name)
    # print (f.name)
    # print (f.value)
    # print ("失败" is f.value)
    # print(TaskStatus.value)
    print("running"==TaskStatus.running.name)
