"""
*args: type(args)结果为元组
"""
def f(*args):
    print(args, type(args))

l = [1, 2, 3, 4]
# 不加*,把对象本身加入元组
f(l)
# 如果加*的话,会将对象里的每个元素都拆开加入元组
f(*l)

"""
**kwargs:type(kwargs)结果为字典
"""
def f2(**kwargs):
    print(kwargs, type(kwargs))

f2(list=[1, 2, 3])

"""
在对函数传值时,究竟是值传递还是引用传递,我认为要分情况
对于不可变类型,如字符串 元组等是值传递
对于可变类型,如字典 列表等是引用传递
"""
def df1(a):
    a[0] = "a"

a = {0: "1", 1:"2", 2:"3"}
df1(a)
print(a)
