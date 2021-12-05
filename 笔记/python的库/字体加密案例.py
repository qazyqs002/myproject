"""
字体加密
网站示例：
"""


from fontTools.ttLib import TTFont

# 1、请求字体库
# 2、字体库处理
fi = TTFont("字体文件的路径")
fi.saveXML("存储路径")

# 3、取字体映射关系
font_map = fi['cmap'].getBestMap()
# 4、替换文中对应内容

