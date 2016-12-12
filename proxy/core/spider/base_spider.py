#!/usr/bin/env python
# encoding: utf-8


import bs4
from config import HEADER


class BaseSpider(object):

    header = HEADER

    def spider(self):
        pass

    def parse(self):
        pass

    def parse_content(self, text):
        return bs4.BeautifulSoup(text, 'html.parser')
