#!/usr/bin/env python
# encoding: utf-8

str = 'hello python'
test = 10
def greet_you(name):
    global str,test
    str = 'hello ' + name
    test += 100
    return str

print(greet_you('Robbin'))
print('str =', str)
print('test =',test)
