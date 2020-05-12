# 匹配以“www”起始且以“.com”结尾的Web域名，例如:“www.baidu.com”
import re

s1 = "https://www.baidu.com"
s2 = "https://www.zju.edu.cn"
pattern = r"w{3}\.[a-zA-Z]+\.com"     # 正则表达式

print(re.search(pattern, s1).group()) # 匹配成功，返回配置字符串
print(re.search(pattern, s2))         # 匹配失败，返回None