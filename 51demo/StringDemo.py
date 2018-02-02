# 移除字符串头尾指定的字符（默认为空格）
name = "0jack0,jay"
print(name.strip("0"))
# 拆分
name2 = name.split(",")
print(name2)
# 拼接
name3 = "|".join(name2) # 0jack0|jay
name4 = "|".join(name)  # 0|j|a|c|k|0|,|j|a|y
print(name3)
print(name4)
# 字符串格式化
msg = "hello,{name},your age is {age}"
msg2 = "hello,{0},your age is {1}"
msg3 = msg.format(name="jack", age=22)
msg4 = msg2.format("jack", 22)
print(msg3)
print(msg4)
# 填充
str = "jack jay";
print(str.center(40, "="))
# 寻找下标,返回第一个出现的下标
print(str.find("jj"))