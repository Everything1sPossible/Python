import keyword
import sys
# 注释
"""
注释
"""
'''
注释
'''

keyword.kwlist
print("hello,python!")
if True:
    print("true")
else:
    print("false")
word = '这是一个字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(word)
print(sentence)
print(paragraph)
# input("\n\n按下 enter 键后退出。")
x = "runboo"; sys.stdout.write(x + "\n")
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)