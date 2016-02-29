#!/usr/bin/env python
# encoding: utf-8

def showComment(str):
    print('\n' + 10 * '*' + str + 10 * '*' + '\n')

# Python's string

## String Basic
showComment('String Basic')
print("isn't, he said") # 单引号
print('isn\'t, he said') # 双引号
print(r'C:\some\name') # r 原字符
print('''show multiple lines string
show multiple lines string
show multiple lines string''') #多行字符
print(3 * ("Don't " + "repeat " + "youself "))
print('Put several strings within parentheses '
      'to have them joined together.')
for w in 'Python':
    print(w)

## String Method
showComment('String Method')

### 1 capitalize() 首字母大写
str = 'string'
print('str = {0}'.format(str))
print('str.capitalize() = ' + str.capitalize())

### 2 lower() 小写转换
str = 'ABC'
print('str = %s' % (str))
print('str = %s' % (str.lower()))

### 3 upper() 大写转换
str = 'abc'
print('str = %s' % (str))
print('str = %s' % (str.upper()))

### 4 count() 返回重复字符的个数
###   参数：1.需要查找到字符
###         2.相应的range
str = 'aaabbbccc'
print('str = ' + str)
print("str.count('a') = %d" % str.count('a'))
print('str.count(\'a\') = %d' % str.count('a',0,3))

