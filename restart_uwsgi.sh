#!/bin/bash

ps aux|grep uwsgi.ini|grep -v grep|awk '{print $2}'|xargs kill -9

sleep 1.5

ulimit -n 65535

uwsgi --ini uwsgi.ini

ps aux|grep uwsgi.ini|head -3


ps aux|grep pyspider|grep -v grep|awk '{print $2}'|xargs kill -9
