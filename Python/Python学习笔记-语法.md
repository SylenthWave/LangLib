# Python学习笔记之语法
> 很多人都说Python是入门非常简单的语言，非常适合那些没有编程经验的初学者。这话没错，因为Python的语法确实非常简练。写起来也非常的优雅，所以接下来就着重学习一下Python的语法。

## 常量
在Python中不能声明定义一个常量，一切只能靠我们开发者自己掌控。但和其他语言类似的是，定义一个常量一般使用大写变量名。**但实际上它还是可变的**。
```Python
PI = 3.14159
CONST_VALUE = 100
```
由于缺少了特定语法，开发者只能自己控制常量和变量的使用。如果一不小心给“常量”赋值，那么结果可想而知。当然你还是有机会弥补这个错误，比如使用如下方式定义常量：

```Python
def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):
    @constant
    def FOO():
        return 0xBAADFACE
    @constant
    def BAR():
        return 0xDEADBEEF

CONST = _Const()

print CONST.FOO
##3131964110

CONST.FOO = 0
##Traceback (most recent call last):
##    ...
##    CONST.FOO = 0
##TypeError: None
```
这段代码很简单的解决了之前的问题

1. 定义一个constant函数，如果是调用getter返回参数实例，如果调用setter抛出异常
2. 这样当我们给使用了这个函数创建的对象赋值的时候就会被抛出一个异常，所以它一个read-only属性。
3. 使用常量函数可以快速创建一个read-only属性，这样我们就可以创建一个有错误保护机制的常量类。

## 变量
声明一个变量非常简单，不需要类型只需要指定一个变量名就可以了。起名字是程序员最痛苦的事情，不过一个意义明了的变量名是非常重要的，因为它关乎了我们程序的可读性。Python中的变量名是区分大小写的,`var=10`和`Var=10`不同。对于一般变量通常使用小写开头的变量名。如果一个单词不能表达变量意思的时候可以使用`_`进行连接,总之一个有意义的变量名对我们写出好程序的意义是非常重要的。

```Python
var = 100
print(var) # 100
var = 10
print(var) # 10
```

处理单一的赋值方式，还可以同时声明多个变量。

```Python
var1,var2,var3 = 0,1,2
# var1 = 0
# var2 = 1
# var3 = 2

[var1,var2,var3] = [0,1,2]
# var1 = 0
# var2 = 1
# var3 = 2

(var1,var2,var3) = (0,1,2)
# var1 = 0
# var2 = 1
# var3 = 2
```

## 操作符
基本操作`+`,`-`,`*`,`/`,`%`都非常简单就不多说了。    
说说特殊的
* 幂操作符`**`
    `v = 2**3 # 2*2*2 = 8`
* 取最近整数操作符 `//`
    `v = 13//3 # 4`
    `v = -13//3 # 5`
* 位移操作符
    * 左移：`2 << 2 = 8`
        由于2的二进制数为`0010`，它向左移两位后为`1000`，而`1000`的10进制数为8。
    * 右移：`2 >> 1 = 0`
        由于2的二进制数为`0010`，它向右移两位后为`0001`，而`0001`的10进制数为1。
* 逻辑操作符
    * 逻辑或`or` `|`
    * 逻辑与`and` `&`
    * 逻辑非`not` `!`

## 控制流
下面开始说说Python中的控制流    

`if` `while` `for` `break` `continue` 就是Python中的控制流关键字。在Python中使用空格而非`{}`来确定表达式关系。这与其他语言有所区别。

* `if` 条件判断表达式

    ```python
    num = 10
    if num > 10:
        print('num > 10')
    elif num == 10:
        print('num = 10') # num = 10
    else:
        print('num < 10')
    ```
    请注意：在Python中不使用`{}`而是使用空格替代，`else if` 简化为`elif`。


* `while` 条件判断循环表达式

    ```python
    num = 0
    while num < 10:
        print(num)
        num += 1
    else:
        print('end')
    # 0 1 2 3 4 5 6 7 8 9 end
    ```
    请注意：`while`支持else，这是Python的特色哦。插一句 Python不支持 ++ --，所以上述表达式使用的是：`num += 1`

* `for` 循环表达式

    ```python
    for num in range(10):
        print(num)
    else:
        print(end)
    # 0 1 2 3 4 5 6 7 8 9 end
    ```
    请注意：`for`同样支持else哦。还有Python中只支持`for-in`一种形式的for循环，不能使用像c语言那种形式的for循环。`range()`函数可以控制循环次数。

    ```python
    item = [1,2,3,4]
    for num in item:
        print(num)
    else:
        print(end)
    # 1 2 3 4 end
    ```
    这是使用`for-in`遍历一个数组。如果我需要数元素的index怎么办？

    ```python
    item = [1,2,3,4]
    for idx,num in enumerate(item):
        print(idx)
        print(num)
    else:
        print(end)
    # 0 1 1 2 2 3 3 4 end
    ```
    使用`enumerate()`函数来解决这个问题。

* `break` 跳出

    如果你在一块控制流代码中不想执行剩下的代码了，那么可以使用`break`关键字跳出代码块。

    ```python
    for num in range(10):
        print(num)
        if num == 5:
            break
    else:
        print(end)
    # 0 1 2 3 4 5
    ```
    请注意：`break`直接跳出循环，并且不会执行`else`中的语句。

* `continue` 跳出本次循环

    使用`continue`语句可以跳出控制流中本次循环之后的代码，使用也很简单。

    ```python
    for num in range(10):
        if num == 5:
            continue
        print(num)
    else:
        print(end)
    # 0 1 2 3 4 6 7 8 9 end
    ```

## 函数

#### 定义
函数是什么呢？就是一段有名字的代码块嘛。在Python中使用`def`关键字定义一个函数。既然是函数就会有相应的参数和返回值。在Python中我们并不需要显示的指定参数和返回值类型。甚至我们都**不需要写返回值类型**。因为Python默认隐式的为我们的函数添加了返回类型。

```python
def input_yourname(name):
    return 'hello ' + name
print(input_yourname('Python')) # hello Python
```

#### 文档字符串
上面函数的参数是name，由于Python的特性，name这个参数实际上可以是任意类型。但是当我们使用的时候，最好又一些说明来告知函数的使用者。所以就有了文档字符串。

```python
def input_yourname(name):
    """print hello yourname param name is str type"""
    return 'hello ' + name
print(input_yourname('Python')) # hello Python
print(input_yourname.__doc__) # print hello yourname param name is str type
```

#### 局部变量
函数中的变量都是局部变量。当我们为函数赋值的时候，实际上它是对外部变量进行了copy，为其创建了一个同名变量，所以当改变函数体内部变量的值时并不会影响外部变量。

```python
x = 10
def changeX(x):
    print(x) # 10
    x += 10
    print('change x to',x) # change x to 20
changeX(x)
print('x = ',x) # x = 10
```

#### `global`全局变量

使用`global`关键字可以在函数内部改变外部变量的值。需要注意的是，使用`global`的方式是`global + 变量名`。可以同时声明多个全局变量，使用`,`分隔变量名即可。

```python
str = 'hello python'
test = 10
def greet_you(name):
    global str,test
    str = 'hello ' + name
    test += 100
    return str

print(greet_you('Robbin')) # hello Robbin
print('str =', str) # str = hello Robbin
print('test =',test) # test = 110
```

#### 函数默认值

你可以为函数创建一个默认值以便当没有参数时函数也会做出默认反应，在函数参数后边加上`=`并赋上相应的值即可。

```python
def show_name(name='please enter your name',times=1):
    print(name * times)

show_name() # please enter your name
show_name('robbin') # robbin
```

**注意**：函数参数默认值是根据位置(index)定位的，所以如果你给一个参数设置了默认值，那么此参数后边的所有参数必须有默认值，不然视为不合法。

```python
def show_name(name='please enter your name',times):
    print(name * times)

    # SyntaxError: non-default argument follows default argument
```

在调用某个函数时，你可以指定设置某个参数值，其他参数使用默认参数

```python
def show_name(name='please enter your name',times=1):
    print(name * times)

show_name(times=2) # RobbinRobbin
show_name(name='Robbin') # Robbin
```

**注意**：当默认参数是可变对象时，该默认参数的指针总会指向可变对象的内存地址。

```python
def add(item, s=[]):
    s.append(item)
    print(s)

add(1)    # [1]
add(1,[]) # [1]
add(1)    # [1,1]
```

从上面代码可以看出，函数默认参数的是一个变量，这个变量的指针在函数创建时被创建，指向默认参数提供的数组。当第二次调用函数时我们为默认参数提供了一个新数组，所以它会指向改数组的内存地址。但当我们继续调用函数并继续使用默认参数时，它又重新指向最初创建数组的地址。如何解决这个问题？

```python
def add(item, s=None):
    if s == None:
        s = []
    s.append(item)
    print(s)

add(1)    # [1]
add(1,[]) # [1]
add(1)    # [1]
```

函数参数还可以定义一个可变参数，一般使用`*argument_name`表示一个元组，使用`**argument_name`表示一个数组。

```python
def add(*num):
    print(len(num)) # 4
add(1,2,3,4)
```

```python
def add(**dic):
    print(len(dic)) # 3
add(var1=1,var2=2,var3=3)
```

`pass`关键字表示空代码块

```Python
def func():
    pass
```







