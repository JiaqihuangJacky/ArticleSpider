# -*- coding: utf-8 -*-
__author__ = 'bobby'
import hashlib
import re


def get_md5(url):
    #check if unique code, stc is unique
    #if yes then make it to utf-8
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == "__main__":
    print (get_md5("http://jobbole.com".encode("utf-8")))