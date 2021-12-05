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

