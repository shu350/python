import urllib.request
import re      #导入urllib.request库
b = str(input("请输入："))   #提示用户输入信息，并强制类型转换为字符串型
a = urllib.request.urlopen(b)#打开指定网址
html = a.read()              #读取网页源码
html = html.decode("utf-8") #解码为unicode码
pattern1 = '<.*?(href=".*?").*?'
# 根据规则提取出该网页中包含的链接
content_href = re.findall(pattern1,html,re.I)
#print(html)                  #打印网页源码
print(content_href)
