# a = b = c = 1
# print(a)
# print(b)
# print(c)
# print("=============================")
# d, e, f = 1, 2, "hello"
# print(d)
# print(e)
# print(f)
# ============================================
"""
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
    例子:
    class A:
    pass

    class B(A):
    pass

    isinstance(A(), A)  # returns True
    type(A()) == A      # returns True
    isinstance(B(), A)    # returns True
    type(B()) == A        # returns False
"""
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))
# ==================================
# 字符串
# 字符串不可以改变
str = "hello world"
print(str)           # 输出字符串
print(str[0: -1])    # 输出第一个到倒数第二个所有字符串
print(str[2: 5])     # 输出第三个到第五个字符串
print(str[2])        # 输出第三个字符串
print(str[2:])       # 输出第三个到最后的所有字符串
print(str * 2)       # 输出两次字符串
print(str + "test")  # 拼接字符串
print('he\nllo')
print(r'he\nllo')

# 列表
mylist = ['a', 'b', 'c', 'd']
mylist1 = ['e', 'f', 'g']
print(mylist)
print(mylist[0: 2])
print(mylist[2])
print(mylist * 2)
print(mylist + mylist1)
# list元素可以被改变
mylist[0: 2] = []
print(mylist)

# 元组
tuple = ('a', 'b', 'c', 'd')
tuple1 = ('e', 'f')
print(tuple)
print(tuple[0: 2])
print(tuple[2])
print(tuple * 2)
print(tuple + tuple1)
# list与元组可以互相包含
tuple2 = ('g', mylist)
print(tuple2)
mylist2 = ['g', tuple]
print(mylist2)

# set集合
set1 = {'a', 'b', 'c', 'd', 'a'}
print(set1)
if('a' in set1):
    print('a在集合中')
else:
    print('a不在集合中')
a = set('abcd')
b = set('cdef')
print(a)
print(b)
print('=======================')
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# 字典
dict = {}
dict['one'] = '1'
dict['two'] = '2'
dict1 = {'a': '1', 'b': '2'}
print(dict);
print(dict['one'])
print(dict.keys())
print(dict.values())
print(dict.items())
for k, v in dict.items():
    print(k, ':', v)
def example(a, b):
    return (a, b)
print(example(3,4))
print(type(example(3,4)))
def test(*args):
    print(args)
    return args
print(type(test(1,2,3,4)))
def example2(dict):
    for d in dict:
        print(d, ':', dict[d])
example2(dict)