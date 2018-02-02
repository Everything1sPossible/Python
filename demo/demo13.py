# # 打开一个文件
# f = open("D:/foo.txt", "w")
# num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!")
# print(num)
# # 关闭打开的文件
# f.close()
# """
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
# """
# # 打开一个文件
# f1 = open("D:/foo1.txt", "w")
#
# value = ('www.runoob.com', 14)
# s = str(value)
# f1.write(s)
# print(f1.tell())
# # 关闭打开的文件
# f1.close()

"""
pickle模块:python的pickle模块实现了基本的数据序列和反序列化。
      通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
      通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
"""
# 序列化
# import pickle
# dict1 = {
#     1: "1",
#     2: "2",
#     3: "3"
# }
# tuple1 = (1, 2, 3)
# list1 = [1, 2, 3]
# file = open("D:/foo2.txt","wb")
# pickle.dump(dict1,file)
# pickle.dump(tuple1,file)
# pickle.dump(list1,file)
# file.close()

# 反序列化
import pickle
import pprint

# 使用pickle模块从文件中重构python对象
pkl_file = open('D:/foo2.txt', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

data3 = pickle.load(pkl_file)
pprint.pprint(data3)

pkl_file.close()