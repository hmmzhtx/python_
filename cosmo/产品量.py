# -*- coding:utf-8 -*-
import urllib
#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
from bs4 import BeautifulSoup
# from scrapy.selector import Selector
# from scrapy.selector import HtmlXPathSelector
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


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
        # if (tds[0].get_text() in txt_arr):
        #     if(int(tds[2].get_text()) < 10):
        #         proName = tds[0].get_text()
        #         subNum = tds[2].get_text()
        #         pro_num = proName + u',' + subNum
        #         pro_txt.append(pro_num.encode("utf-8"))
        #         # all_txt.append(pro_txt)
        #         # all_txt = all_txt.join(u'--------').join(proName).join(u'还剩余：').join(subNum)
        #         # print all_txt
        #         return pro_txt
        #         # print '--------',tds[0].get_text(),'还剩余：',tds[2].get_text()



if __name__ == '__main__':
    mac_pro_arr = [
                       ['护肤类-卸妆','http://2019.cosmopolitan.com.cn/project.html?cid=9']
                   ]

    for mac_pro in mac_pro_arr:
        list = get_pro(mac_pro[1])
        if list:
            print mac_pro[0]
            for nn in list:
                print '------:'+ nn