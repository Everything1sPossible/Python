"""
输出格式化
"""
for i in range(1, 11):
    print("{0} {1} {2}".format(i, i*i, i*i*i))
print('==============================')
# rjust:将字符串靠右, 并在左边填充指定长度的字符串,默认空格
# rjust(2, "*"):此时就是补*
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))
# 在数字的左边填充 0
s = "abc"
print(s.zfill(5))
# format用法
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math
print('常量 PI 的值近似为： {!s}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))