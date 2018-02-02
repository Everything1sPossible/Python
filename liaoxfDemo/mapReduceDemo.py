from functools import reduce


# 求和
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


# 求乘积
def f2(x):
    return x * x


li = [1, 2, 3, 4, 5]
print(list(map(f2, li)))


print(tuple(map(str, [1, 2, 3, 4])))


def fn(a, b):
    return a * 10 + b


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))

print(reduce(lambda x, y: x * 10 + y, map(char2num, '13579')))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[0].upper() + name[1:].lower()


print(list(map(normalize, ['adam', 'LISA', 'barT'])))


def mul(c, d):
    return c * d


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(mul, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    # 将数字字符串转为数字序列
    nums = map(lambda n: CHAR_TO_FLOAT[n], '123.456')
    # 标记
    point = 0

    def to_float(f, g):
        # global关键字用来在函数或其他局部作用域中使用全局变量。
        # nonlocal 适用于在局部函数中的局部函数,把最内层的局部变量设置成外层局部可用，但是还不是全局的。
        nonlocal point
        # 如果遇到. 原数返回,并将point转为1
        if g == -1:
            point = 1
            return f
        # 如果标记为0,说明还没遇到.
        if point == 0:
            return f * 10 + g
        # 如果遇到. 就换算法 .后的数字每遇到一次就多除以10,
        else:
            # 将point每次以10倍增长
            point = point * 10
            return f + g / point
    return reduce(to_float, nums)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


