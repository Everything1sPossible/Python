print(sorted([36, 5, -12, 9, -21]))


print(sorted([36, 5, -12, 9, -21], key=abs))

from operator import itemgetter
"""
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）
"""
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
"""
请用sorted()对上述列表分别按名字排序：
"""
print(sorted(L, key=lambda x: x[0]))
"""
再按成绩从高到低排序：
"""
print(sorted(L, key=lambda x: x[1], reverse=True))

print(sorted(L, key=itemgetter(0)))
print(sorted(L, key=lambda t: t[1]))
print(sorted(L, key=itemgetter(1), reverse=True))

