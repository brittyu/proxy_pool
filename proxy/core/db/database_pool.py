#!/usr/bin/env python
# encoding: utf-8


import MySQLdb
from DBUtils.PooledDB import PooledDB
from proxy_pool.config import DBHOST, DBPORT, DBUSER, DBPWD, DBCHAR, DBNAME


class DatabasePool(object):

    _pool = None

    def __init__(self):
        pass

    @staticmethod
    def _getConn():
        if DatabasePool._pool is None:
            _pool = PooledDB(
                            creator=MySQLdb,
                            mincached=1,
                            maxcached=30,
                            host=DBHOST,
                            port=DBPORT,
                            user=DBUSER,
                            passwd=DBPWD,
                            db=DBNAME,
                            use_unicode=False,
                            charset=DBCHAR,
                            cursorclass=DictCursor)

            return _pool.connection()
