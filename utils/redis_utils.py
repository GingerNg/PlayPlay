#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/7/18 3:01 AM
# @Author  : lixintang - (xintang.li@fir.ai)
# @Site    : 
# @File    : redis_utils.py


class RedisInstance(object):

    def __init__(self, redis_type=None, **args):
        if redis_type == "cluster":
            import rediscluster
            self.r_conn = rediscluster.StrictRedisCluster(**args)
        else:
            import redis
            self.r_conn = redis.StrictRedis(**args)

    def get_value(self, name):
        return self.r_conn.get(name)

    def incr_value(self, name):
        return self.r_conn.incr(name)

    def set_value(self, name, value):
        self.r_conn.set(name, value)

    def getset_value(self, name, value):
        return self.r_conn.getset(name, value)


if __name__ == '__main__':
    # 单点
    conn_dict = {
        'host': '127.0.0.1',
        'port': 6379
    }

    redis_type = 'single'
    redis_instance = RedisInstance(redis_type, **conn_dict)
    print(redis_instance.set_value('name', 'test'))
    print(redis_instance.get_value('name'))
    print(redis_instance.getset_value('name', 0))
    print(redis_instance.get_value('name'))

    # cluster
    # conn_dict = {
    #     "startup_nodes": [
    #         {'host': '127.0.0.1', 'port': 9001},
    #         {'host': '127.0.0.1', 'port': 9002},
    #         {'host': '127.0.0.1', 'port': 9003}
    #     ]
    # }
    # redis_type = 'cluster'
    # myredis = RedisInstance(redis_type, **conn_dict)
    # print(myredis.SetValue('name', 'test'))
    # print(myredis.GetValue('name'))
    # print(myredis.GetSetValue('name', 0))
    # print(myredis.GetValue('name'))