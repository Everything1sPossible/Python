"""
用filter求素数
    计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
    首先，列出从2开始的所有自然数，构造一个序列：
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
    取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
    取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
    5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
    取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
    7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
    不断筛下去，就可以得到所有的素数。
"""


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
"""
=========================================================================================
"""
"""
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
"""


def is_palindrome(n):
    sn = str(n)
    snlen = len(sn)
    if snlen == 1:
        return n
    elif snlen == 2:
        if sn[0] == sn[1]:
            return n
    else:
        if (snlen % 2) > 0:
            snlenh = snlen // 2 + 1
        else:
            snlenh = snlen // 2
        if sn[::-1][:snlenh] == sn[:snlenh]:
            return n


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


