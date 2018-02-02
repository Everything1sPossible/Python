list = [[321, 3213], 312321, 3213, 123, 123123, 1235324, 234234]
# 往尾部添加对象
list.append(222)
print(list)
# 添加对象,第一个参数为添加的对象在列表中的位置,第二个参数为对象
list.insert(0, 333)
print(list)
# 计算数量,只会搜索最外层的列表
print('count:', list.count(3213))
# 出现的位置,默认查找第一个,只搜索最外层列表
print(list.index(3213))
# 将所有的3213替换成111
for i in range(list.count(3213)):
    list[list.index(3213)] = 111
print(list)
# 拼接合并
list1 = ['打算', '大声道', 111]
list.extend(list1)
print(list)
print(list1)
# 反转
list.reverse()
print(list)
# 排序(3.x里数字和字符串不可以一起排,2.x里可以一起排)
list2 = [321, 3213, 312321, 3213, 123, 123123, 1235324, 234234]
list2.sort()
print(list2)
# 移除列表对象,默认最后一个,参数为移除的对象坐标
list3 = [[321, 3213], 312321, 3213, 123, 123123, 1235324, 234234]
list3.pop(0)
print('list3:', list3)
"""
复制列表
如果列表内部嵌套列表,只copy最外层列表,内部嵌套的多层列表都共享.
也就是说列表内部如果嵌套列表,实际上最外层列表里存的是内部列表的内存指针,该指针指向内存中的内部列表,
这样做的好处就是,如果内部列表数据量很大的话,可以节省内存空间
"""
# 借助copy库进行深copy,可以完全复制
import copy
list4 = [321, 3213, 312321, [3213, [123, 6767]], 123123, 1235324, 234234]
list5 = list4.copy()
list6 = copy.deepcopy(list4)
list4[0] = 9999999999
list4[3][0] = 8888888888
list4[3][1][0] = 7777777
print('list4:', list4)
print('list5:', list5)
print('list6:', list6)
print('list4[3].id:', id(list4[3])) # 39429192
print('list5[3].id:', id(list5[3])) # 39429192
print('list6[3].id:', id(list6[3])) # 39450696




