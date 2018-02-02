import getpass
"""
跟着alxe学python
"""
"""
输出结果name=jay是因为name变量重新指向"jay"对象,而name2=jack是因为,虽然定义了name2=name,
但是实际上只是把name2这个变量指向了"jack"对象,所以虽然name的指向发生了变化,但是并不影响name2的指向.
"""
# name = "jack"
# name2 = name
# name = "jay"
# print(name)
# print(name2)
#
# res = map(lambda x: x**x, range(10))
# print(res)
#
# name = input("输入您的姓名:")
# sex = input("输入您的性别:")
# age = int(input("输入您的年龄:"))
# print("name is %s, sex is %s, age is %d" %(name, sex, age))
'''
getpass模块在pycharm客户端中使用不和谐
在windows小黑板下可以正常使用
'''
# username = input("username :")
# password = input("password :")
# print(username, password)
# if username == "sjh" and password == "sjh":
#     print("输入正确!")
# else:
#     if username != "sjh":
#         print("用户名错误!")
#     else:
#         print("密码错误!")
# for i in range(10):
#     print(i)
age = 22
# while int(input("请输入年龄:")) != age:
#     print("年龄错误!")
for i in range(10):
    inage = int(input("age is :"))
    if inage == age:
        print("age is true!")
        break
    elif inage > age:
        print("age is much biger!")
    else :
        print("age is much smaller!")
