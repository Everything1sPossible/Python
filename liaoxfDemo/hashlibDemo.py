import hashlib, hmac

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))  # d26a53750bc40b38b65a520292f69306
print(md5.hexdigest())

sha1 = hashlib.sha1()
# 如果数据量很大，可以分块多次调用update()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

message = b'Hello, world!'
key = b'secret'
# 随机key，原始消息message，哈希算法
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
