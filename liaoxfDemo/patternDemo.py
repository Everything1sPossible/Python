"""
正则表达式:
    用\d可以匹配一个数字，\w可以匹配一个字母或数字,\s可以匹配一个空格
    .可以匹配任意字符,用*表示任意个字符（包括0个），
    用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符,
    由于'-'是特殊字符，在正则表达式中，要用'\'转义
    要做更精确地匹配，可以用[]表示范围，比如：
        1.[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
        2.[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
        3.[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串;
        4.[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
        5.A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
        6.^表示行的开头，^\d表示必须以数字开头。
        7.$表示行的结束，\d$表示必须以数字结束。
        8.你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
        9.使用Python的r前缀，就不用考虑转义的问题了.
"""
import re


s = '010-12345'
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
if re.match(r'^\d{3}\-\d{3,8}$', s):
    print('ok')
else:
    print('fault')
# 切分
s1 = 'a,b;; c  d'
r = re.split(r'[\s\,\;]+', s1)
print(r)
"""
分组
group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
"""
m = re.match(r'^(\d{3})-(\d{3,8})$', s)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())
# 时间匹配正则表达式
t = '19:05:30'
m1 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:'
              r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:'
              r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m1.groups())
"""
预编译正则表达式
"""
# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
m2 = re_telephone.match('010-12345')
print(m2.groups())

# 邮箱匹配
s_email1 = 'someone@163.com'
s_email2 = 'bill.gates@microsoft.com'
s_email3 = 'bob#example.com'


def is_valid_email(addr):
    re_email = re.compile(r'^([0-9a-zA-Z\_\.]+)\@([0-9a-zA-Z]+)(.com|.org)$')
    if re_email.match(addr):
        return True
    else:
        return False


print(is_valid_email(s_email1))
print(is_valid_email(s_email2))
print(is_valid_email(s_email3))


