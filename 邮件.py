import smtplib
from email.mime.text import MIMEText
s = '1563773187@qq.com'
a = 'zirhmitzesligedh'
r = '2467884397@qq.com'
subject = '简单邮件'
context = 'hello 爱你'

msg = MIMEText(context,'plain','utf-8')
msg['Subject'] = subject
msg['From'] = s
msg['To'] = r
try:
    server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
    print('成功连接到邮件服务器')
    server.login(s, a)
    print('成功登录邮箱')
    server.sendmail(s, r, msg.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送异常')
finally:
    server.quit()
