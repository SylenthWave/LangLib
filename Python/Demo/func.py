#!/usr/bin/env python
# encoding: utf-8

"""
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

def show_yourname(name='Mengdiji',times=1):
    print(name * times)

show_yourname()
show_yourname('jimengdi')
show_yourname(times=10)

def add(item, s=[]):
    s.append(item)
    print(len(s))

add(1)     # 1
add(1)     # 2
add(1, []) # 1
add(1, []) # 1
add(1)     # 3

def cal_count(**num):
    print(num)

cal_count(hello=1)
"""
def add(item, s=None):
    if s == None:
        s = []
    s.append(item)
    print(s)

add(1)
add(1)
add(1)
add(1,[])
add(1)






