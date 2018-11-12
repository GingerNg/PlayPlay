# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: mongo_utils.py
@time: 2018/4/16 9:59
"""
import json
import os
from io import BytesIO
import sys

import bson
from pymongo import MongoClient, ReturnDocument

# from utils.constants import DataStatus


def insertFile(file_path):
    """
    insert file whose size < 16M into mongodb
    :param file_path:
    :return:
    """
    try:
        fin = open(file_path, "rb")
        img = fin.read()
        data = BytesIO(img)
        fin.close()
        # conn = MongoClient('10.101.12.23', 27017)
        conn = MongoClient('101.132.167.173', 8003)
        db = conn.mydb
        coll = db.test_set
        with open(file_path, 'rb') as myimage:
            content = BytesIO(myimage.read())
            coll.save(dict(
                content=bson.binary.Binary(content.getvalue()),
                filename=file_path.split(".")[0],
                file_format=file_path.split(".")[1]
            ))
    except Exception as e:
        print (e)
        sys.exit(1)
    # finally:
    #     imgput.close()  todo


def file_read_binary(plugin_name,file_path = None):
    """
    从mongo中读文件，文件为二进制
    :return:
    """
    try:
        # fin = open(os.path.join(file_path,plugin_name), "wb")
        # img = fin.read()
        # data = StringIO(img)
        # fin.close()
        conn = MongoClient('101.132.167.173', 8003)
        db = conn.mydb
        files = db.test_set
        res = files.find_one({"filename":plugin_name})
        fin = open(os.path.join(file_path, plugin_name)+"."+res["file_format"], "wb")
        print (res)
        content = res['content']

        fin.write(content)
        # print('sum:', files.count())
        # insertimg = imgput.put(data)
        # print insertimg
    except Exception as e:
        print (e)
        sys.exit(1)

def _get_connection(url):
    return MongoClient(url)

def _get_db(url,db):
    client = _get_connection(url)
    return client[db]

def _get_coll(url,db,coll_name):
    db = _get_db(url,db)
    return db[coll_name]


def search(url,db,coll_name,filter = {}):
    collection = _get_coll(url = url,db=db,coll_name=coll_name)
    return collection.find(filter)


def fetch_one(url,db,coll_name,filter = {}):
    collection = _get_coll(url = url,db=db,coll_name=coll_name)
    # return collection.find_one(filter)
    return collection.find_one_and_update(filter,
                                        {"$set": {"status": "1"}},
                                        return_document=ReturnDocument.AFTER)



def get_collection_names(url):
    """
    获取mongodb所有数据库对应的collection名
    :param url:
    :return:
    """
    client = _get_connection(url)
    d = dict((db, [collection for collection in client[db].collection_names()])
             for db in client.database_names())
    return d


def update_one(url, db, coll_name, filter={}, data={}):
    collection = _get_coll(url=url, db=db, coll_name=coll_name)
    collection.update_one(filter=filter, update={"$set": data})
    # db.stu.update_one({"age": 18}, {"$set": {"age": 100}})


def insert_one(url, db, coll_name, data={}):
    collection = _get_coll(url=url, db=db, coll_name=coll_name)
    collection.insert_one(document=data)


def save_or_update_one(url,db,coll_name, filter={}, data={}):
    collection = _get_coll(url=url, db=db, coll_name=coll_name)
    record = collection.find_one(filter=filter)
    if record:
        # 更新
        collection.update_one(filter=filter, update={"$set": data})
    else:
        # 插入
        collection.insert_one(document=data)


if __name__ == "__main__":
    # print (search(url = 'mongodb://101.132.167.173:8013/',db="mydb",coll_name="test_clean")[0]["result"])
    print (get_collection_names(url='mongodb://101.132.167.173:8014/')["pyspider_resultdb1"])
    # result = fetch_one(url='mongodb://101.132.167.173:8014/',
    #              db="mydb",
    #              coll_name="test_clean",
    #              filter={'status': {'$exists': 1}})
    # print(result)
    # if result:
    #     print("00")
    # else:
    #     print("11")
