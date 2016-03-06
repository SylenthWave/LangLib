#!/usr/bin/env python
# encoding: utf-8

def constant(f):
    def fset(self,value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget,fset)

class _Const(object):
    @constant
    def FOO():
        return 100


CONST = _Const()
print(CONST.FOO)
CONST.FOO = 10000
