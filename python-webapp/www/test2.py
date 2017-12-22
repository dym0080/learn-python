# -*- coding: utf-8 -*-

def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        yield alist.pop(c)
a = ["aa","bb","cc"]
c=mygen(a)
print(c)
