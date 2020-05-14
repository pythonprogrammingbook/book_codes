# 请基于request库开发一个下载网页图片并保存的程序

import shutil
import requests

url = 'http://www.dgut.edu.cn/images/listimg.jpg'  # 网站图片的URL

response = requests.get(url, stream=True)
with open('img.jpg', 'wb') as img_file:
    shutil.copyfileobj(response.raw, img_file)
del response