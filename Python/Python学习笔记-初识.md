## 初识Python

> 今天开始正式学习Python，并记下笔记。一定要坚持下去，每天进步一点点~

### Python基础

Python是一种计算机编程语言。计算机编程语言和我们日常使用的自然语言有所不同，最大的区别就是，自然语言在不同的语境下有不同的理解，而计算机要根据编程语言执行任务，就必须保证编程语言写出的程序决不能有歧义，所以，任何一种编程语言都有自己的一套语法，编译器或者解释器就是负责把符合语法的程序代码转换成CPU能够执行的机器码，然后执行。Python也不例外。

#### 1.输入输出
1. 输出
每个语言的第一个程序都是Hello world嘛，而使用Python输出Hello World非常简单，只需使用`print()`函数即可。
```Python
print('Hello World') #输出Hello World
print('Hello','World') #同样也输出Hello World，在print()函数中用“,”(其中","相当于一个空字符)可以连接两个字符串。
```
2. 输入
输入使用`input()`函数，它会将你输入的字符作为返回值返回给你，所以你需要使用一个变量来储存这个值。
```Python
name = input()
print('input() =',name)
```

现在结合输入输出函数就可以写出一个简单的问答程序了

```python
print('Please enter your name:')
username = input()
print('Ok, Now enter \'q\' input your name')
key = input()

if key == 'q':
print('hello,',username)
```
代码非常简单。

#### 2.注释

注释Python的注释不同于我们平时学习的语言，*它用#作为注释*而不是用`\\`。
```Python
#comment with python
```


