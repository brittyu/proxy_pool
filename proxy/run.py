#!/usr/bin/env python
# encoding: utf-8

from spiders.xicidaili import Xicidaili


check = Xicidaili()
for item in check.parse():
    print item
