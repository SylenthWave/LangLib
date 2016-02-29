# 初识Python

> 今天开始正式学习Python，并记下笔记。一定要坚持下去，每天进步一点点~

Python是一门流行的脚本语言，许多我们熟知网站的后端语言都是Python。如知乎、豆瓣等等。它也是一门非常适合新手的语言，入门非常容易，当然如果你想深入学习的话还是需要下一些功夫的。这篇笔记主要是用来记录我自己学习Python的过程，因为它并不是我的工作语言，所以我想把学习过程记录下来更加有助于日后的复习吧。下面就直接进入正题了:)

## 一、输入输出

**输出**    
每个语言的第一个程序都是Hello world嘛，而使用Python输出Hello World非常简单，只需使用`print()`函数即可。
```Python
print('Hello World')   #输出Hello World
print('Hello','World') #同样也输出Hello World，在print()函数中用“,”(其中","相当于一个空字符)可以连接两个字符串。
print('Hello',end=)
print('World',end=)    ##print()函数总是会自动带一个换行符，使用end=可以取消换行符
```
**输入**    
输入使用`input()`函数，它会将你输入的字符作为返回值返回给你，所以你需要使用一个变量来储存这个值。
```Python
name = input()
print('input() =',name)
```

现在结合输入输出函数就可以写出一个简单的问答程序了,代码非常简单。

```python
print('Please enter your name:')
username = input()
print('Ok, Now enter \'q\' input your name')
key = input()

if key == 'q':
print('hello,',username)
```

## 二、注释

注释Python的注释不同于我们平时学习的语言，**Python使用`#`作为注释**而不是用`\\`。
```Python
#comment with python
```

## 三、整型/浮点

整形和浮点类型是Python主要的两种数字类型。
`2`表示一个整数，而`3.22`或`322E-4`表示一个浮点数。
> 值得注意的是Python没有单独的long、short类型，整数类型可以表示任意的大小。

## 四、字符串的基本用法

### 转义

Python中定义一个字符串变量可以使用单引号或者双引号。`\ ` 同大部分语言一样，表示转义字符。
```Python
str1 = "Isn't, he said."   #Isn't, he said
str2 = 'Isn\'t, he said.'  #Isn't, he said
```

那么当你在字符串中需要使用`\ `时怎么办呢？有两种方法:

* 使用`\\`
    ```Python
    print('C:\\some\\name')  #C:\some\name
    ```
* 使用`r`
    ```Python
    print(r'C:\some\name') # r = raw strings,也就是原字符串。#C:\some\name
    ```

`format()`方法是一种类似OC中`%`的占位替换函数,使用起来也非常简单。
```Python
str = "hello"
print('{0} world'.format(str)) #Hello world
```

### 连接

Python还提供了多行字符的表示方法，使用使用`"""`或`'''`来表示多行字符
```Python
mutStr = '''This is a multiple lines string
use \"Triple Quotes\" to show the multiple string'''
print(mutStr)

# This is a multiple lines string
# use "Triple Quotes" to show the multiple string

```

Python还可以使用`+`和`*`来连接字符串。
```Python
print(3 * ("Don't" + " repeat " + "youself, ")) #Don't repeat youself, Don't repeat youself, Don't repeat youself
```

如果你想把一个长字符串拆分成多段也非常简单
```Python
print('Put several strings within parentheses '
      'to have them joined togather.') #Put several strings within parentheses to have them joined togather.'
```

### 下标方法

Python的字符串类型是支持下标方法的，所以你可以利用index获取相应的字符。另外**Python中的字符串是不可变的**，所以你不能给字符下标赋值。
```Python
word = 'Python'
print(word[0])               #P
print(word[-1])              #n
print(word[0:2])             #Py
print(word[0:2] + word[2:])  #Python
for w in word:               # P y t h o n
    print(w)

word[0] = 'N'                #TypeError
```

### 字符串相关方法

**大小写转换方法**

`Capitalized()`方法用于字符串的首字符大写
```Python
### 1 capitalize() 首字母大写
str = 'string'
print('str = {0}'.format(str))
print('str.capitalize() = ' + str.capitalize())
```
`lower()`将字符串转换成小写形式
```Python
### 2 lower() 小写转换
str = 'ABC'
print('str = %s' % (str))
print('str = %s' % (str.lower()))
```

`upper()`将字符串转换成大写形式
```Python
### 3 upper() 大写转换
str = 'abc'
print('str = %s' % (str))
print('str = %s' % (str.upper()))
```
































