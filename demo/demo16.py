"""
os模块提供了不少与操作系统相关联的函数。
"""
import os
os.getcwd()      # 返回当前的工作目录
"""
针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
"""
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
"""
glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
"""
import glob
print(glob.glob('*.py'))
"""
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
"""
import sys
print(sys.argv)
"""
sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。
"""
sys.stderr.write('Warning, log file not found starting a new one\n')
"""
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
"""
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
"""
math模块为浮点运算提供了对底层C函数库的访问:
"""
import math
math.cos(math.pi / 4)
math.log(1024, 2)
"""
random提供了生成随机数的工具。
"""
import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(5))
"""
访问 互联网
有几个模块用于访问互联网以及处理网络通信协议。
其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib
"""
from urllib.request import urlopen
for line in urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    # if 'EST' in line or 'EDT' in line:  # look for Eastern Time
    print(line)
"""
日期和时间
datetime模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
该模块还支持时区处理:
"""
from datetime import date
now = date.today()
print(now)
"""
以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
"""
import zlib
s = '你好'.encode()
print(len(s))
# 中文压缩首先要把字符串转为bytes
t = zlib.compress(s)
print(len(t))
b = zlib.decompress(t)
print(b.decode())

print(zlib.crc32(s))
"""
性能度量
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。
相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。
"""
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
"""
测试模块
开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:
unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
"""
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试