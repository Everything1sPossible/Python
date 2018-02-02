"""
偏函数demo
"""
import functools


str = '1000'
# print(int(str))
# print(type(int(str)))

print(int(str, base=2))

int2 = lambda x, base=2: int(x, base)
print(int2('1000'))
"""
简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
"""
int3 = functools.partial(int, base=2)
print(int3('1000'))