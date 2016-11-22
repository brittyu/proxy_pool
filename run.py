#!/usr/bin/env python
# encoding: utf-8

import bs4
import time
import MySQLdb
import requests
from random import randint

__author__ = 'brittyu'

base_url = 'http://www.xicidaili.com/nn/%s'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': 1
}


def main():
    for response in page_request(base_url, headers):
        soup = parse_content(response.text)
        tr_list = soup.find(id='ip_list').find_all('tr')
        del tr_list[0]
        ip_list = [(item.find_all('td')[1].string, item.find_all('td')[2].string) for item in tr_list]
        insert_sql(ip_list)


def page_request(base_url, headers):
    for page_index in range(1, 100):
        time.sleep(randint(1, 10))
        yield requests.get(base_url % str(page_index), headers=headers)


def insert_sql(data):
    db = MySQLdb.connect('localhost', 'root', 'yxs', 'proxy_pool')
    cursor = db.cursor()

    for item in data:
        insert_sql = 'insert into proxy_pool value ("%s", "%s")' % (item[0], item[1])
        cursor.execute(insert_sql)
    db.commit()


def parse_content(text):
    return bs4.BeautifulSoup(text, 'html.parser')


if __name__ == '__main__':
    main()
