# 添加
s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
# s1.difference(s2):s1中存在,s2中不存在的值
s1 = {11, 22, 33}
s2 = {33, 44, 55}
print(s1.difference(s2))
# s1.symmetric_difference(s2):s1与s2交集之外的值
print(s1.symmetric_difference(s2))
# s3.difference_update(s4):先取到s3中存在,s4中不存在的值,然后将s3更新为该值
s3 = {11, 22, 33}
s4 = {33, 44, 55}
s3.difference_update(s4)
print(s3)
# s5.symmetric_difference_update(s6):先取到s5与s6交集之外的值,然后把s5更新为该值
s5 = {11, 22, 33}
s6 = {33, 44, 55}
s5.symmetric_difference_update(s6)
print(s5)
"""
discard:移除指定的值,如果不存在不报错
remove:移除指定的值,如果不存在报错
pop:随机移除某值,并可以返回该值
"""
# s7 = {11, 22, 33}
# s7.discard(4444)
# s7.remove(4444)
# s7.pop()
# print(s7)
# s8.intersection(s9):s8与s9的交集
s8 = {11, 22, 33}
s9 = {33, 44, 55}
print(s8.intersection(s9))
# s8.intersection_update(s9):先取到s8与s9的交集,然后更新s8为该值
s8.intersection_update(s9)
print(s8)
# s10.union(s11):s10与s11的并集
s10 = {11, 22, 33}
s11 = {33, 44, 55}
print(s10.union(s11))
# 批量更新:参数为可迭代的
s12 = {11, 22, 33}
l = [1, 2, 3]
s12.update(l)
print(s12)