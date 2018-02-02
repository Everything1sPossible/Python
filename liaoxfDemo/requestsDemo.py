import requests

# r = requests.get('https://www.douban.com/')
# # 状态码
# status = r.status_code
# # 数据
# data = r.text
# print('Status:', status)
# print('Data:', data)

# # 对于带参数的URL，传入一个dict作为params参数：
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# # 实际请求的地址url
# print(r.url)

# # requests自动检测编码，可以使用encoding属性查看
# print(r.encoding)

# # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
# print(r.content)

# # requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
# r = requests.get('https://query.yahooapis.com/v1/public/yql?'
#                  'q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# 需要传入HTTP Header时，我们传入一个dict作为headers参数
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)
print(r.headers)
print(r.cookies)

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)

# 要在请求中传入Cookie，只需准备一个dict传入cookies参数
# cs = {'token': '12345', 'status': 'working')
# r = requests.get(url, cookies=cs)

# 要指定超时，传入以秒为单位的timeout参数
# r = requests.get(url, timeout=2.5) # 2.5秒后超时
