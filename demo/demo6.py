import sys

# list = [1, 2, 3, 4]
# it = iter(list)    # 创建迭代器对象
# print(type(it))
# print(next(it))   # 输出迭代器的下一个元素
# print(next(it))
# for x in it:
#     print(x, end=" ")
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
"""
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
"""
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        print('a:%d,b:%d' % (a, b))
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()