"""
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
"""
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中


    def inner():
        i_count = 2  # 局部作用域
"""
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这这些语句内定义的变量，外部也可以访问。如下代码:
实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
"""
if True:
    msg = "true"
print(msg)

"""
函数内可以访问全局变量，但不能更新(修改)其值！
"""
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)

fun1()
print(num)

