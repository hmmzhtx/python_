# -*- coding:utf-8 -*-
import urllib
#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '574895690@qq.com'  # 发件人邮箱账号
my_pass = 'gdxvkonzbrscbcje'  # 发件人邮箱密码
my_user = 'huangmingming@zzss.com'  # 收件人邮箱账号，我这边发送给自己

## u'滴露衣物除菌液', ,u'趣拿限时惠-滴露'
txt_arr = [u'康如洗护套装',u'零感避孕套',u'便携式衣服粘滚',u'趣拿限时-妙洁',u'趣拿限时惠-杰士邦',u'趣拿限时惠-康如']

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')

def get_pro(url):
    html = getHtml(url) #获取该网址网页详细信息，得到的html就是网页的源代码
    soup = BeautifulSoup(html,"html.parser")
    table = soup.table
    tr_arr = table.find_all("tr")

    pro_txt = []

    for tr in tr_arr:
        tds = tr.find_all('td')
        if (tds[0].get_text() in txt_arr):
            if(int(tds[2].get_text()) < 10):
                proName = tds[0].get_text()
                subNum = tds[2].get_text()
                pro_num = proName + u',' + subNum
                pro_txt.append(pro_num.encode("utf-8"))
                # all_txt.append(pro_txt)
                # all_txt = all_txt.join(u'--------').join(proName).join(u'还剩余：').join(subNum)
                # print all_txt
                return pro_txt
                # print '--------',tds[0].get_text(),'还剩余：',tds[2].get_text()



if __name__ == '__main__':
    mac_pro_arr = [
                       ['友谊商场4层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/73'],
                       ['华士达影城正大乐城店1号楼3层','http://brand.zzss.com:8084/fet/fet/citylist/1/1006/1005'],
                       ['古北1699商业广场B1层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/1123'],
                       ['汇阳广场3层B','http://brand.zzss.com:8084/fet/fet/citylist/1/1006/1155'],
                       ['鹿都国际购物广场4层','http://brand.zzss.com:8084/fet/fet/citylist/1/10062/1199'],
                       ['绚荟城2层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/2199'],

                       ['顺恒国际商业广场1层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/s1580'],
                       ['车配龙生活欢乐港4层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/s1578'],
                       ['汇金奥特莱斯南商场B2层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/s1488'],
                       ['汇金奥特莱斯北商场B2层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/s1489'],
                       ['华士达影城浦江店4层','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/1047'],
                       ['巴黎春天七宝店1层A','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/1279'],
                       ['巴黎春天七宝店1层A','http://brand.zzss.com:8084/fet/fet/citylist/1/10005/1205'],

                       ['大宁国际A', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1013/s1874'],
                       ['珺悦18广场B座2层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1010/s1559'],
                       ['大宁国际商业广场12座3层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/10011/19'],
                       ['新邻生活广场B2层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1014/146'],
                       ['香港名都2层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1014/1053'],
                       ['香港名都3层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1014/1052'],

                        ['宝地广场C区1层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1004/57'],
                        ['王子百货1层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/10011/80'],
                        ['太平洋百货不夜城店1层B', 'http://brand.zzss.com:8084/fet/fet/citylist/1/10011/251'],
                        ['华士达影城宝山店3层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1009/1046'],
                        ['巴黎春天五角场店1层', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1004/1092'],
                        ['太平洋生活广场1层A', 'http://brand.zzss.com:8084/fet/fet/citylist/1/1004/1187']
                   ]

    for mac_pro in mac_pro_arr:
        list = get_pro(mac_pro[1])
        if list:
            print mac_pro[0]
            for nn in list:
                print '------:'+ nn


        # get_pro(mac_pro[1])
        # result = get_pro(mac_pro[1])
        # print result;
        # try:
        #     msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        #     msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        #     msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        #     msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题
        #
        #     server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        #     server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        #     server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        #     server.quit()  # 关闭连接
        #     print("邮件发送成功")
        # except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        #     print("邮件发送失败")