import re,time
import datetime
import requests
# import pymysql
import xlwt
import l_tool
import threading
import json

"""一、时间格式转换"""
# str = "【发布时间 ：2019年11月26日 10:00:45】"
# m = re.findall(r'\d+',str)
# print(m)

"""二、今天时间时间生成和昨天时间 以及转换成str格式"""
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days=1)
# today =today.strftime('%Y-%m-%d')
# yesterday =yesterday.strftime('%Y-%m-%d')
# print(today)
# print(type(today))
# print(yesterday)
# print(type(yesterday))

"""三、时间戳的转换(18位时间戳跟13位的时间戳)"""
# now_time_1 = time.time() # 18位时间戳
# print(now_time_1)
# now_time_2 = int(round(time.time() * 1000))  # 13位时间戳
# print(now_time_2)

"""四、当前小时的获取"""
# now_hour =  datetime.datetime.now().hour
# print(now_hour)

"""五、字符串的%s代表原来的含义，不是占位符"""
# 其他几个占位符也同理
# str = "Hello %s, %%s" % 'world!'
# print(str)

"""六、操作excel表格"""
# # 1、创建表格任务对象
# form = xlwt.Workbook()
# # 2、创建单个表格任务对象
# mysheel = form.add_sheet("test1")
# # 3、插入对象
# mysheel.write(0,0,"u")
# mysheel.write(0,1,"w")
# mysheel.write(0,2,"e")
# # 4、保存
# form.save("tesa.xlx")

"""七、字符串去除空格"""
# st = " s  ds d "
# print(st)
# a = st.strip()
# print(a)

"""八、上传数据的模板"""
# l_title = "北京市轨道交通一票通非接触式IC卡车票供应商入围选定(2021年-2023年）招标公告"
# l_file_url = "http://bulletin.cebpubservice.com/project/2021-01/noticeFile/Z1101000420002525001/68d7d524f8aa47ffab7c3a9fee564b3e.swf"
# l_con = '''<object width="100%" height="100%" id="_349543931" name="_349543931" data="http://bulletin.cebpubservice.com/FlexPaperViewer.swf" type="application/x-shockwave-flash">
#                                    <param name="allowfullscreen" value="true">
#                                    <param name="allowscriptaccess" value="always">
#                                    <param name="quality" value="high">
#                                    <param name="flashvars" value="SwfFile={}&amp;Scale=0.6&amp;ZoomTransition=easeOut&amp;ZoomTime=0.5&amp;ZoomInterval=0.05&amp;FitPageOnLoad=true&amp;FitWidthOnLoad=true&amp;ProgressiveLoading=true&amp;MinZoomSize=0.05&amp;MaxZoomSize=5&amp;InitViewMode=Portrait&amp;ViewModeToolsVisible=true&amp;ZoomToolsVisible=true&amp;NavToolsVisible=true&amp;CursorToolsVisible=true&amp;localeChain=zh_CN"><param name="wmode" value="transparent">
#                                    </object>'''.format(l_file_url)
#
#
# info = tool.Save(l_title, 30022, 9, 20, 6, 19, 20, 30022, l_con, "2021-01-20", 1)
# info.save_backstaget()

"""九、后台查重的模板"""
# l_title = "关于学生公寓空气能热泵更换工程项目的答疑公告"
# l_time = "2021-01-03"
# l_sa = tool.Data_deduplication(l_title, 0, 0, 0).post()
# print(l_sa)

"""十、检测是否时间格式"""
# 判断爬下来的是否是时间格式
# a = "2019-12-5"
# try:
#     b = datetime.datetime.strptime(a, '%Y-%m-%d')
# except:
#     print("不是时间格式")
# else:
#     print("是时间格式")

"""十一、后台获取城市编号"""
# a = tool.Return_label("福建","上海").get_num()
# print(a)

"""十二、多线程例子"""
# def print1():
#     print("111")
# def print2():
#     print("222")
# thre1 = threading.Thread(target=print1)
# thre2 = threading.Thread(target=print2)
# thre1.start()
# thre2.start()
# thre1.join(timeout=30)
# thre2.join(timeout=30)

"""十三、selenium跟PIL库截取验证码图的例子"""
# from selenium import webdriver
# from PIL import Image
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# driver.save_screenshot('baidu.png')
# ele = driver.find_element_by_xpath('//div[@id="lg"]/img[1]')
# left = ele.location["x"]   # 左上角横坐标
# top = ele.location["y"]  # 左上角纵坐标
# right = left + ele.size["width"]  # 右下角横坐标
# botton = right + ele.size["height"]  # 右下角横坐标
# im = Image.open("baidu.png")
# im_crop = im.crop((left,top,right,botton))
# im_crop.save("logo.png")
# driver.quit()

"""十四、后台上传文件"""
# import tool
# import requests
# m = "https://zcy-gov-open-doc.oss-cn-north-2-gov-1.aliyuncs.com/1023FP/330299/100032675/201912/6606c154-6c2c-47f0-a26d-268a4693b603"
# files = [
#     ("attach[]",('filename1.doc',requests.get(url=m).content)),
#     ("attach[]",('filename1.doc',requests.get(url=m).content))
# ]
# info = tool.Save('测试1',30007,104, 20, 6, 228, 233, 30007,'测试1','2019-12-19',1,h_file=files)
# info.save_backstaget()

"""十五、判断时间大小"""
# import requests
# import re
# import datetime
# # from datetime import datetime
# today = datetime.date.today()
# today_11 = datetime.datetime(today.year, today.month, today.day)
# a = "2019-12-20"
# dd = datetime.datetime.strptime(a, "%Y-%m-%d")
# dd_11 = datetime.datetime(dd.year, dd.month, dd.day)
# print(dd)
# print(type(dd))
# if dd_11 < today_11:
#     # dd_1的时间在today时间前边
#     print("1")
# else:
#     print("2")

"""十六、tkinter可视化窗口"""
# import tkinter
# # 创建TKinter库对象
# top = tkinter.Tk()
# li = ["c","python"]
# def click_1():
#     a = t.get("1.0","end")
#     print(a)
# # 设置插入按钮
# b1 = tkinter.Button(text="确认",width=20,height=2,command=click_1)
# b1.pack()
# # 设置文本框
# t = tkinter.Text(width=20,height=2)
# t.pack()
# top.mainloop()

"""十七、logging输出日志"""
# import logging
# logging.basicConfig(filename='tool/output.log',level=logging.ERROR, format='%(filename)s - %(asctime)s - %(module)s - %(levelname)s - %(message)s')
#
# logger = logging.getLogger(__name__)
#
# logger.info("this is a log info")
# logger.debug('Debug')
# logger.warning('Warn')
# logger.info("Finish")
# logger.error("this is a error")

"""十八、十三位时间戳转换成正常时间格式"""
# import time
# timeNum = 1590678677000
#
# timeStamp = float(timeNum/1000)
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)

"""十九、中文的url编码"""
# a = "流标公示表（二次）.doc"
# from urllib import parse
# a = a.encode('gb2312')
# print(a)
# b = parse.quote(a)
# print(b)

"""二十、selenium实例"""
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # 设置无头浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# # 创建selenium对象
# driver = webdriver.Chrome(chrome_options=chrome_options)
# # 超时设置
# driver.set_page_load_timeout(5)
# driver.set_script_timeout(5)
# driver.get('http://zfcg.qingdao.gov.cn/sdgp2014/site/channelall370200.jsp?colcode=0401&flag=0401#')
# time.sleep(2)
# print(driver.page_source)

"""二十一、剔除标题的标签"""
# try:
#     title_tag = h_content.xpath("./p[1]")[0]
#     title_tag.getparent().remove(title_tag)
# except:
#     pass

"""二十二、python 标准库之shutil"""
# 文件的拷贝了等等
# swfextract用来处理flash文件，在cmd中运行

"""二十三、CST时间用python转换"""
# l_time = "Thu Aug 27 15:36:27 CST 2020"
# time_struct = time.strptime(l_time, "%a %b %d %H:%M:%S CST %Y")
# l_time = time.strftime("%Y-%m-%d %H-%M-%S", time_struct)

"""二十四、swf文件上传到后台然后获取文件链接"""
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
# }
# l_file_url = "http://ecp.cnmc.com.cn/project/2020-10/809d0787748c479194d80e7b43a24946//6a72513a9c314d78b20770c7e9bce77a.swf"
# l_file_con = requests.get(url=l_file_url, headers=headers)
# l_file_src = tool.get_file_src("{}".format(l_file_url), l_file_con)
# print(l_file_src)

"""二十五、aes加密"""
# from Crypto.Cipher import AES
# import base64
# import requests
# import json
# import time
# import datetime
# from lxml import etree
# from urllib import parse
# from PIL import Image
#
# # https://ggzyfw.fj.gov.cn/web/index.html#/business/list?timeType=6&KIND=GCJS&PROTYPE=A01&BeginTime=2020-03-03%2000%3A00%3A00&EndTime=2020-09-03%2023%3A59%3A59
#
# s = requests.session()
#
#
# def decrypt(enStr):
#     """内容aes方式解密"""
#     key = b"BE45D593014E4A4EB4449737660876CE"
#     iv = b"A8909931867B0425"
#     enStr = bytes(enStr, encoding = "utf8")
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     # enStr += (len(enStr) % 4)*"="
#     # decryptByts = base64.urlsafe_b64decode(enStr)
#     decryptByts = base64.b64decode(enStr)
#     msg = cipher.decrypt(decryptByts)
#     # paddingLen = ord(msg[len(msg)-1])
#     return msg.decode()

"""二十六、后台通过标题删除数据"""
# with open("a.txt", "r", encoding='utf-8') as f:
#     l_txt = f.read()
# a = l_txt.split("\n")
#
# with open("b.txt", "r", encoding='utf-8') as p:
#     l_b = p.read()
# b = l_b.split("\n")
# c = []
# for i in a:
#     if i in b:
#         pass
#     else:
#         c.append(i)
# print(len(c))
#
# for every_title in c:
#     time.sleep(2)
#     h_title = every_title
#     url = "http://ad13in.gc-zb.com/publiccon/select_tit"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
#         "Cookie": "__jsluid_h=52d15d62259b2eacdb97ee6b798f5b6a; client_login_info=787bgZWVwnq_wxO2Th_pCtIw8JZIFcW.shxjslodYzXD2GAJi8dKEdDGQlsAaWZw779QdM1.ciOzy56I; clientlogin=fc1bMkLYGP1VIHhlLSNmWICTI3w8sH6VGFWW73v6WYFbqL5984czsOGX.rp3CnNCOD9otWnVVp9tq_Fkiy46HiBiiECwfFTv9Reb49YIhQdeFv4b; Hm_lvt_2bcf2125a6023661c7c71e9111ae9d53=1574936150,1575008143,1575079864,1575343234; Qs_lvt_278260=1574816307%2C1574936150%2C1575008143%2C1575079862%2C1575343233; Qs_pv_278260=3893670450121527000%2C3952495039439689000%2C2970218440000754700%2C2416788784359911000%2C307773907429302900; PHPSESSID=ee5i07935j4ibp9c5vq8n45ivm; userlogin=6ea4.iNW83gMcAsetZN3r7eSPAlzRKxMJUB3CzWuvBgqt2z7st16FQbRF5Iy3pDWKqJD5usr5tKeV66na_NbaF06gkIMMB_RJV51VErTnCx3XtwzHx2dLjpogfvjAMySXL.RhVF5QdBXRpc; login_info=6ea4.iNW83gMcAsetcEg_.eaMQwtEKpMdEsjDDiuvhhY9Gzks8FjEnSTFI8z3pDLIvUZ5A",
#     }
#     data = {
#         "title": h_title,
#         "province":'',
#         "time": '',
#         "infoid": '',
#     }
#     response = requests.post(url=url, headers=headers, data=data, timeout=20)
#     html = response.content.decode('utf-8')
#     h_body = json.loads(html)
#     print(h_body)
#     if h_body["msg"] == "找到了数据":
#         if "{}".format(h_body["data"][0]["code"]) == "30128":  # 限制编号为30128
#             chk = h_body["data"][0]["nid"]
#             del_url = "http://ad13in.gc-zb.com/infomation/del.html"
#             data_1 = {
#                 "pid":"",
#                 "title":"",
#                 "infoid": "0",
#                 "classid": "0",
#                 "s_time": "",
#                 "e_time": "",
#                 "search_field": "0",
#                 "province": "0",
#                 "chk[]": "{}".format(chk),
#             }
#             res = requests.post(del_url,headers = headers,timeout=15,verify=False,data =data_1)
#             with open("b.txt", "a", encoding='utf-8') as y:
#                 y.write(h_title)
#                 y.write('\n')
#         else:
#             pass
#     else:
#         print("后台未找到数据")
