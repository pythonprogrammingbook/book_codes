import requests #导入request库
# 反网站防爬
HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
# 网页的URL
URL = "https://www.baidu.com"

# 请求网页数据
r = requests.get(url=URL, headers=HEADERS)
# 打印状态信息
print(f"status code:{r.status_code};encoding:{r.encoding}")
# 打印网页HTTP源代码
print("HTTP Source Code:")
print(r.content.decode())
