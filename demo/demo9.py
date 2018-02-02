"""
将列表当做堆栈使用:
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，
最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。
用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
"""
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
"""
将列表当作队列使用:
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
"""
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
"""
列表推导式:列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边#第一条语句是最后一层。
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
如果希望表达式推导出一个元组，就必须使用括号。
"""
list = [1, 2, 3, 4]
list1 = [3*i for i in list]
print(list1)
list2 = [[i, 3*i] for i in list]
print(list2)
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
newfreshfruit = [weapon.strip() for weapon in freshfruit]
print(newfreshfruit)
# if做过滤器
list3 = [3*x for x in list if x > 2]
print(list3)
# 其他循环技巧
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
newvec = [x*y for x in vec1 for y in vec2]
print(newvec) #[8, 6, -18, 16, 12, -36, 24, 18, -54]
"""
嵌套列表解析
"""
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
newmatrix2 = [[row[i] for row in matrix] for i in range(4)]
print(newmatrix2) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print("======================================")
for i in range(4):
    for row in matrix:
        print(row[i], end=" ")