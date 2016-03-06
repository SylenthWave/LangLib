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









