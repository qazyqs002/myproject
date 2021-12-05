"""
python中对字符串的 五种加密方式以及代码
"""

"""一、url编码 以及解码"""
# from urllib import parse
# str1 = '{"pageSize":10,"pageIndex":2,"title":"","type":"001"}'
# str2 = parse.quote(str1)    #将字符串进行编码
# print(str2)
#
# str3 = "%7B%27pageSize%27%3A%2010%2C%20%27pageIndex%27%3A%201%2C%20%27title%27%3A%20%27%27%2C%20%27type%27%3A%20%27002%27%7D"
# str3 = parse.unquote(str3)  #解码字符串
# print(str3)

"""二、base64编码解码"""
# import base64
# # base64 编码
# e = base64.b64decode("4444")
# # base64解码
# c = base64.b64encode(e)
# print(e)
# print(c)
"""三、 字符串转换ascii"""
# name = "王大"
# # 编码
# ascii_name = list(map(ord, name))
# # print(ascii_name)
# # 解码
# l_name = "".join(map(chr, ascii_name))
# print(l_name)

"""四、md5 不可逆"""
import hashlib

name = '123456'
l_md5 = hashlib.md5(name.encode()).hexdigest()
print(l_md5)

"""五、 Unicode 转中文"""
name = "王大锤"
# 编码
unicode_name = name.encode('unicode_escape')
utf8_name = name.encode("utf-8")
gbk_name = name.encode('gbk')
gb2312_name = name.encode("gb2312")

# 解码
l_unci = unicode_name.decode('unicode_escape')
l_utf8_name = utf8_name.decode()  # 默认是utf-8   括号内可以带utf-8
l_gbk_name = gb2312_name.decode('gbk')  # gb2312 属于gbk的一种
print(l_gbk_name)
