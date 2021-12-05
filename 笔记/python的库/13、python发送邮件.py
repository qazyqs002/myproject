import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

# 发送邮件
def send_email(send_data):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = ''
    password = ''
    # 收信方邮箱
    to_addr = '1448334428@qq.com'

    # 发信服务器
    smtp_server = 'smtp.qq.com'
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText('{}'.format(send_data), 'plain', 'utf-8')
    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('通报状态{}'.format(time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))))

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr.split(','), msg.as_string())
    print('邮件发送成功.....')
    # 关闭服务器
    server.quit()


send_email('yqs-python测试')


