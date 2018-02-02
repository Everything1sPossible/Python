import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
"""
Python发送邮件demo
"""
def sendmail():
    mail_smtp = "smtp.163.com"  # 设置发件服务器
    smtp_post = 25  # 发件服务器端口
    mail_user = "s563149980@163.com"  # 用户名
    mail_pass = "s563149980"  # 口令
    email_text = "测试111111111111111"  # 邮件内容
    subject_text = "测试"  # 主题
    sender_name = "宋家辉163"  # 发送方名称
    sender = 's563149980@163.com'  # 发送方
    receivers_name = "宋家辉qq"  # 接收方名称
    receivers = '563149980@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 邮件正文
    msg = MIMEText(email_text, "plain", "utf-8")
    # 发件人
    msg["From"] = formataddr([sender_name, sender])
    # 收件人
    msg["To"] = formataddr([receivers_name, receivers])
    # 邮件主题
    msg["Subject"] = subject_text
    try:
        # 创建一个SMTP对象,连接到smtp主机
        server = smtplib.SMTP(mail_smtp, smtp_post)
        # 启动安全传输模式
        server.starttls()
        # 登录
        server.login(mail_user, mail_pass)
        # 发送邮件
        server.sendmail(sender, [receivers], msg.as_string())
        server.quit()
        print("邮件发送成功!!!")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


"""
Python发送带附件邮件demo(有BUG,尚未解决)
"""
def sendmailWithMul():
    mail_smtp = "smtp.163.com"  # 设置发件服务器
    smtp_post = 25  # 发件服务器端口
    mail_user = "s563149980@163.com"  # 用户名
    mail_pass = "s563149980"  # 口令
    sender = 's563149980@163.com'  # 发送方
    receivers = '563149980@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("宋家辉163", 'utf-8')
    message['To'] = Header("宋家辉qq", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText('这是Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('D:/a.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="a.txt"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    att2 = MIMEText(open('D:/b.txt', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="b.txt"'
    message.attach(att2)

    # try:
    # 创建一个SMTP对象,连接到smtp主机
    server = smtplib.SMTP(mail_smtp, smtp_post)
    # 启动安全传输模式
    server.starttls()
    # 登录
    server.login(mail_user, mail_pass)
    # 发送邮件
    server.sendmail(sender, [receivers], message.as_string())
    server.quit()
    print("邮件发送成功!!!")
    # except smtplib.SMTPException as e:
    #     print("Error: 无法发送邮件")
    #     print(e)

