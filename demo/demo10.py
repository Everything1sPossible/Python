dict1 = {
    1: "jack",
    2: "jay",
    3: "jay"
}
list1 = list(dict1.values())
set1 = set(dict1.values())
print(list1)
print(set1)
"""
zip()组合俩列表
"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
"""
反向遍历
"""
for x in range(10, -1, -1):
    print(x)
for x1 in reversed(range(1, 10, 2)):
    print(x1)
"""
对列表进行去重排序
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
