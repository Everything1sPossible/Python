"""
字符串下,name2变量等于name变量,改变name变量值,实际上就是把name变量重新指向另一个内存地址,而name2变量不变..
而在列表下,list5变量等于list4变量,改变list4变量里的任一值,但是list4变量的指针指向不变,list5的指针指向也不变,
但是数据发生变化,这是因为这两个变量都指向同一个内存地址
"""
name = "aaa"
name2 = name
name = "bbbb"
print(id(name))
print(id(name2))

list4 = [321, 3213, 312321, [3213, [123, 6767]], 123123, 1235324, 234234]
list5 = list4
list4[3][1][0] = 88888
print(list4)
print(list5)
print(id(list4))
print(id(list5))

list6 = []
list7 = []
for i in range(0, 10):
    list6.append(9999)
for j in range(0, 10):
    list7.append(list6)
list7[0][0] = 0
print('list6:', list6)
"""
此处list7内部的所有列表的0位置的数据都变成了0,这是因为虽然list7[0][0] = 0这样操作,
实际上list6与list7共享该列表的内存地址,修改的是同一份列表
"""
print('list7:', list7)
print(id(list6))
print(id(list7[0]))

graph = [[] for i in range(10)] # 长度为10的空列表
for a in range(0, 10):
    for b in range(0, 10):
        graph[a].append(9999)
graph[0][0] = 0
print(graph)
print(id(graph[1]))
print(id(graph[2]))

