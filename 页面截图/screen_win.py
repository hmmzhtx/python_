#!/usr/local/anaconda3/envs/python27
# -*-coding:utf-8 -*-

import datetime
import pymysql
import DouMail
from selenium import webdriver
from PIL import Image
from time import sleep

def fetch_results():
    flag = 1
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='test', port=3306, charset='utf8')
    cursor = db.cursor()
    sql = "SELECT * FROM screen_url WHERE flag = '{flag}'".format(flag=flag)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def screen_shot(event_id, event_url):
    driver = webdriver.PhantomJS(executable_path='D:/py_tools/phantomjs-2.1.1-windows/bin/phantomjs')

    driver.set_page_load_timeout(5)
    driver.set_window_size('375', '667')
    url = event_url
    driver.get(url)
    sleep(3)

    element = driver.find_element_by_id("mp-header")
    print("获取元素坐标：")
    location = element.location
    print(location)
    print("获取元素大小：")
    size = element.size
    print(size)

    # 计算出元素上、下、左、右 位置
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    img_path = 'C:/work/event_{}.png'.format(event_id)

    driver.save_screenshot(img_path)
    driver.quit()

    im = Image.open(img_path)
    im = im.crop((left, top, right, bottom))
    im.save(img_path)
    return img_path

def send_mail(to_list, title, content, cc_list=[], encode='utf-8', is_html=True, images=[]):
    content = '<pre>%s</pre>' % content
    m = DouMail.Mail('smtp.zzss.com', '465', '黄明明', 'huangmingming@zzss.com', 'H084820h')
    m.send_mail(to_list, title, content, cc_list, encode, is_html, images)

def sendMail(images):
    today = datetime.datetime.today()
    today_str = today.strftime('%Y-%m-%d')
    title = 'KPI 截图 %s' % today_str
    content = '以下为KPI 截图 %s' % today_str
    send_mail(['huangmingming@zzss.com'], title, content, ['huangmingming@zzss.com'], 'utf-8', True, images)


if __name__ == '__main__':
    images = []
    data = fetch_results()
    for row in data:
        img_path = screen_shot(row[0], row[1])
        images.append(img_path)
    sendMail(images)