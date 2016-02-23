## 初识Python

> 今天开始正式学习Python，并记下笔记。一定要坚持下去，每天进步一点点~

### Python基础

#### 输入输出

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

#### 注释

注释Python的注释不同于我们平时学习的语言，*它用#作为注释*而不是用`\\`。
```Python
#comment with python
```


