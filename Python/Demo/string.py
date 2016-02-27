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
showComment("String Method")
str = "string"

### 1 capitalize
print('str = {0}'.format(str))
print('str.capitalize() = ' + str.capitalize())

