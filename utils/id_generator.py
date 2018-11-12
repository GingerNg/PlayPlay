# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: id_generator.py
@time: 2018/4/26 10:08
"""
import time
import uuid


def create_job_id():
    # return "job_"+str(uuid.uuid1())
    return "job_"+ str(int(round(time.time()*1000)))


def create_plugin_id():
    # return "plugin_"+str(uuid.uuid1())
    return "plugin_"+ str(int(round(time.time()*1000)))

def create_task_id():
    # return "plugin_"+str(uuid.uuid1())
    return "task_"+ str(int(round(time.time()*1000)))

def create_script_id():
    # return "plugin_"+str(uuid.uuid1())
    return "script_"+ str(int(round(time.time()*1000)))


def test_job_id():
    # return "job_"+str(uuid.uuid1())
    return "test_"+ str(int(round(time.time()*1000)))


if __name__ == '__main__':
    print(type(create_job_id()))
    print(create_job_id())
    print(create_job_id())
    print(create_plugin_id())