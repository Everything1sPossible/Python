def hello(name):
    print("hello %s !" % (name))

hello("jack")
"""
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
简而言之一句话,不可变的传的都是值,可变的传的都是对象本身
"""


def changeint(a):
    a = 10


a = 'aa'
changeint(a)
print(a)


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)
"""
函数参数分为:必需参数,关键字参数,默认参数,不定长参数
必须参数:  必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
关键字参数:关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
           使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
默认参数:  调用函数时，如果没有传递参数，则会使用默认参数。
不定长参数:你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。
           加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。
           我们也可以不向函数传递未命名的变量。
"""
# 必须参数
# 可写函数说明
def printme(str):
    # "打印任何传入的字符串"
    print(str);
    return;


# 调用printme函数
printme(str = "str");

#关键字参数
# 可写函数说明
def printinfo(name, age):
    # "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="runoob");

# 默认参数
# 可写函数说明
def printinfo2(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    return;


# 调用printinfo函数
printinfo2(age=50, name="runoob");
print("------------------------")
printinfo2(name="runoob");

# 不定长参数

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数:lambda
sum = lambda a, b: a + b
print('相加后的值为:', sum(1, 2))

# return 语句
def sum1(a, b):
    sum1 = a + b
    print('函数内sum1:',sum1)
    return sum1
sum1 = sum1(1, 2)
print('函数外sum1:', sum1)

