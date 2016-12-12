#!/usr/bin/env python
# encoding: utf-8

import bs4
import time
import requests
from random import randint
from core.spider.base_spider import BaseSpider

__author__ = 'brittyu'


class Xicidaili(BaseSpider):
    """
    get http://www.xicidaili.com/ proxy ip
    """

    base_url = 'http://www.xicidaili.com/nn/%s'

    def __init__(self):
        pass

    def spider(self):
        for page_index in range(1, 10):
            time.sleep(randint(1, 10))
            yield requests.get(
                            self.base_url % str(page_index),
                            headers=self.header)

    def parse(self):
        for response in self.spider():
            soup = self.parse_content(response.text)
            tr_list = soup.find(id='ip_list').find_all('tr')
            del tr_list[0]
            ip_list = [(item.find_all('td')[1].string,
                        item.find_all('td')[2].string) for item in tr_list]

            yield ip_list
