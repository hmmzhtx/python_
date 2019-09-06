# -*-coding:utf-8 -*-

import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Mail(object):
    def __init__(self, mail_server, port, nickname, username, password):
        self.mail_server = mail_server
        self.port = port
        self.nickname = nickname
        self.username = username
        self.password = password

    def send_mail(self, to_list, subject, content, cc_list=[], encode='gbk', is_html=True, images=[]):
        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, encode)
        me = str(Header(self.nickname, encode)) + "<" + self.username + ">"
        msg['From'] = me
        msg['To'] = ','.join(to_list)
        msg['Cc'] = ','.join(cc_list)
        if is_html:
            mail_msg = ''
            for i in range(len(images)):
                mail_msg += '<p><img src="cid:image%d" ></p>' % (i+1)
            msg.attach(MIMEText(content + mail_msg, 'html', 'utf-8'))

            for i, img_name in enumerate(images):
                with open(img_name, 'rb') as fp:
                    img_data = fp.read()
                msg_image = MIMEImage(img_data)
                msg_image.add_header('Content-ID', '<image%d>' % (i+1))
                msg.attach(msg_image)
                # 将图片作为附件
                # image = MIMEImage(img_data, _subtype='octet-stream')
                # image.add_header('Content-Disposition', 'attachment', filename=images[i])
                # msg.attach(image)
        else:
            msg_content = MIMEText(content, 'plain', encode)
            msg.attach(msg_content)

        try:
            mail = smtplib.SMTP_SSL(self.mail_server, self.port)  # 连接邮箱服务器
            mail.login(self.username, self.password)
            mail.sendmail(me, to_list + cc_list, msg.as_string())
            mail.quit()
            mail.close()
            print("mail send OK")
            return True
        except Exception as e:
            mail.quit()
            print("mail send False")
            return False

def send_mail(to_list, title, content, cc_list=[], encode='utf-8', is_html=True, images=[]):
    content = '<pre>%s</pre>' % content
    m = Mail('smtp.zzss.com', '465', '黄明明', 'huangmingming@zzss.com', 'H084820h')
    m.send_mail(to_list, title, content, cc_list, encode, is_html, images)


if __name__ == '__main__':
    images = [
        'C:/work/event_1.png',
        'C:/work/event_1.png'
    ]
    today = datetime.datetime.today()
    today_str = today.strftime('%Y-%m-%d')
    title = 'KPI 截图 %s' % today_str
    content = '以下为KPI 截图 %s' % today_str
    send_mail(['huangmingming@zzss.com'], title, content, ['huangmingming@zzss.com'],  'utf-8', True, images)