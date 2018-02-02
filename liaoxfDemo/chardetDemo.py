import chardet

# 检测编码
print(chardet.detect(b'hello world'))  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

data = '鹅,鹅,鹅'.encode('utf-8')
print(chardet.detect(data))  # {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))  # {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))  # 日文{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

