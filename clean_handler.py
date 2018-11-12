

import json
import time

from utils import playplay_config
from utils.datetime_utils import today_now, yesterday_now, timestamp_to_str
from utils.mongo_utils import search, update_one, get_collection_names, insert_one
from utils.constants import CleanStatus, CleanCode

source_url = playplay_config.mongo_url
spider_coll = playplay_config.spider_coll

class CleanHandler(object):

    def __init__(self, source_url, db_name, collections=None, start_time=yesterday_now(), end_time=today_now(), filter={},
                 gather_url=None, gather_db_name=None):
        self.source_url = source_url
        self.db_name = db_name
        self.collections = collections if collections else get_collection_names(url=self.source_url)[self.db_name]
        self.filter = filter
        self.end_time = start_time
        self.start_time = end_time
        self.gather_url = gather_url if gather_url else source_url
        self.gather_db_name = gather_db_name if gather_db_name else "%s_%s" % (db_name, "gather")
        self.gather_collection_news = "%s_%s" % (self.gather_db_name, "news")

    def handle(self):
        stat = {}
        for collection in self.collections:
            results = search(
                url=self.source_url,
                db=self.db_name,
                coll_name=collection,
                filter=self.filter
            )
            success = 0
            failed = 0
            exception = 0
            if results.count() == 0:
                continue
            for result in results:
                try:
                    status = self.handle_one(collection, result)
                except Exception as e:
                    print(e)
                    status = CleanStatus.exception.name

                if status == CleanStatus.succeed.name:
                    success += 1
                elif status == CleanStatus.failed.name:
                    failed += 1
                else:
                    exception += 1

                self.update_result(collection, result['url'], status)

            stat[collection] = {
                "success": success,
                "failed": failed,
                "exception": exception
            }

        return stat

    def handle_one(self, collection, result):

        data = {
            "source_id": result['_id'],
            "url": result["url"],
            "project_name": collection
        }

        spider_data = json.loads(result["result"])
        if "pub_time" not in spider_data:
            data['status'] = CleanStatus.failed.name
            data['err_code'] = CleanCode.no_pub_time.name
            data['err_msg'] = CleanCode.no_pub_time.value
            self.record_handle_result(data)
            return CleanStatus.failed.name

        pub_time = spider_data["pub_time"]  # 时间戳
        # 处理时间 TODO filter content html等相关内容
        try:
            t = self.parse_pub_time(pub_time)
            data['fmt_time'] = t
        except Exception as e:
            data['status'] = CleanStatus.failed.name
            data['err_code'] = CleanCode.parse_pub_time.name
            data['err_msg'] = CleanCode.parse_pub_time.value + e.__str__()
            self.record_handle_result(data)
            return CleanStatus.failed.name

        self.parse_result_to_data(
            spider_data=spider_data,
            data=data
        )
        data['status'] = CleanStatus.succeed.name
        self.record_handle_result(data=data)

        return CleanStatus.succeed.name

    def update_result(self, collection, url, status=CleanStatus.succeed.name):
        update_one(
            url=self.source_url,
            db=self.db_name,
            coll_name=collection,
            filter={'url': url},
            data={'status': status}
        )

    def record_handle_result(self, data):
        insert_one(
            url=self.gather_url,
            db=self.gather_db_name,
            coll_name=self.gather_collection_news,
            data=data
        )

    def parse_pub_time(self, pub_time):

        if not pub_time:
            raise Exception('pub_time 为空')

        try:
            fmt_time = timestamp_to_str(int(pub_time))
        except Exception as e:
            return Exception('pub_time to str err: %s' % e.__str__())

        return fmt_time

    def parse_result_to_data(self, spider_data, data):

        cols = [
            "title",
            "source_name",
            "source_channel",
            "pub_time",
            "fetch_time",
            "inner_url",
            "source",
            "author",
            "editor",
            "keywords",
            "summary",
            "html",
            "content",

            "info_type",
        ]

        for col in cols:
            self.set_key(data, key=col, spider_data=spider_data)

        return data

        # self.set_key(data, key="title", spider_data=spider_data)
        # self.set_key(data, key="source_name", spider_data=spider_data)
        # self.set_key(data, key="source_channel", spider_data=spider_data)
        # self.set_key(data, key="pub_time", spider_data=spider_data)
        # self.set_key(data, key="fetch_time", spider_data=spider_data)
        # self.set_key(data, key="inner_url", spider_data=spider_data)
        # self.set_key(data, key="source", spider_data=spider_data)
        # self.set_key(data, key="author", spider_data=spider_data)
        # self.set_key(data, key="source", spider_data=spider_data)

    def set_key(self, data, key, spider_data):
        data[key] = spider_data[key] if key in spider_data.keys() else ""


def clean_data_handler_job():
    print("资讯数据clean任务开始....", time.localtime(time.time()))
    stat = handler = CleanHandler(
        source_url=source_url,
        db_name=spider_coll,
        filter={
            "status": {"$exists": 0}
        }
    )
    handler.handle()
    print("资讯数据clean任务结束....", time.localtime(time.time()))
    print("资讯数据clean任务结束....", stat)

if __name__ == "__main__":
    clean_data_handler_job()
