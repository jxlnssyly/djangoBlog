# -*- coding: utf-8 -*-

import requests
import random
from django.core.cache import cache

class Joke:
    # 笑话的接口
    def __init__(self):
        self.url = 'http://api.laifudao.com/open/xiaohua.json'


    def get_joke(self):

        joke_data = cache.get('joke_data')
        joke = {}

        if joke_data == None:
            joke_data = requests.get(self.url).json()
            cache.set('joke_data',joke_data,3600)

        # 有笑话
        if joke_data != None:
            random_index = random.randint(0,len(joke_data) - 1)
            joke = joke_data[random_index]
            return joke['content'].replace('\r','').replace('\n','').replace('<br/>','')
        else:
            return ''
