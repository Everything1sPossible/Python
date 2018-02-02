"""
1.Python 编码为 JSON 类型转换对应表：
dict                                    -->	object
list,tuple                              -->	array
str                                     -->	string
int, float, int- & float-derived Enums  -->	number
True                                    -->	true
False                                   -->	false
None                                    -->	null
2.JSON 解码为 Python 类型转换对应表：
object                                  -->	dict
array                                   -->	list
string                                  -->	str
number (int)                            -->	int
number (real)                           -->	float
true                                    -->	True
false                                   -->	False
null                                    -->	None
"""
import json

# python 字典类型数据转为json
data_dict = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
data_list = ["a", "b", "c"]
data_tuple = ("a", "b", "c")

json_dict = json.dumps(data_dict)
json_list = json.dumps(data_list)
json_tuple = json.dumps(data_tuple)
print("python原始dict数据: {0}".format(data_dict))
print("python原始list数据: {0}".format(data_list))
print("python原始tuple数据: {0}".format(data_tuple))
print("dict转换后的json数据: {0}".format(json_dict))
print("lict转换后的json数据: {0}".format(json_list))
print("tuple转换后的json数据: {0}".format(json_tuple))

python_dict = json.loads(json_dict)
print("json转python数据: {0}".format(python_dict))

"""
如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
"""
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}
# 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
    print("json文件的数据: {0}".format(data))