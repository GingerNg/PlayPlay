from django.shortcuts import render

import datetime
import json
import os
from random import randint

import requests
from django.db import transaction

# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view

from utils.logger_utils import get_logging


import threading

from utils.mongo_utils import search
from utils.playplay_config import mongo_url, gather_coll

lock = threading.Lock()

logger = get_logging(__name__)

# Create your views here.


@api_view(['get'])
def word_cloud(request):
    """
    wc
    :param request:
    :return:
    """
    # logger.info(request.path)
    try:
        results = search(url = mongo_url,
               db = gather_coll,
               coll_name = gather_coll,
               filter={})
        for result in results:
            pass
        return render(request, 'wordcloud.html',
                      {'collections': db_amounts,
                       'statistics': objs,
                       'wordcloud':["https://ws1.sinaimg.cn/large/6a6e8236gy1fvh0muucpvj22c0340npe.jpg"]
                       })
    except Exception as e:
        logger.warn("index:%s" % e)
        return render(request, '500.html')