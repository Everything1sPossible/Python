from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

"""
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
"""
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(isinstance(p, Point))
print(isinstance(p, tuple))
"""
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
"""
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
"""
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict.
注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
"""
d = defaultdict(lambda: 'N/A')
d['key1'] = 'abc'
print(d['key1'])
print(d['key2'])
"""
如果要保持Key的顺序，可以用OrderedDict,
注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
"""
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od['x'] = 4
od['z'] = 5
print(od)
"""
Counter是一个简单的计数器，例如，统计字符出现的个数
"""
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)