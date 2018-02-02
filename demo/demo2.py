"""
    python 中的 and 从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值；
    or 也是从左到有计算表达式，返回第一个为真的值；
    其中数字 0 是假，其他都是真；
    字符 "" 是假，其他都是真；
"""
a = 10
b = 20
if ( a and b ):
    print('aaaa')
else:
    print('bbbbb')
a = 0
if ( a and b ):
    print('aaaa')
else:
    print('bbbbb')
# is和==的区别:
# is用于判断两个变量是否引用同一个对象,==用于判断两个变量的值是否相等
if( a is b):
    print("a和b是同一个对象")
else:
    print("a和b不是同一个对象")
if( id(a) == id(b)):
    print("a和b是同一个对象")
else:
    print("a和b不是同一个对象")
b = 10
if( a is b):
    print("a和b是同一个对象")
else:
    print("a和b不是同一个对象")
if( id(a) == id(b)):
    print("a和b是同一个对象")
else:
    print("a和b不是同一个对象")

a = 5000
b = 5000
print(id(a))
print(id(b))
a += 1
print(id(a))
print("我叫%s 今年%d岁" % ("小明", 10))