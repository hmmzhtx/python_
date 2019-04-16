# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from proxy_ip import  proxy_ip
import random

def pv_():
    WIDTH = 320
    HEIGHT = 640
    PIXEL_RATIO = 3.0
    UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
    options = webdriver.ChromeOptions()
    proxy_ip_port = random.choice(proxy_ip)
    proxy_ip_port = '39.135.9.164:80'
    print  proxy_ip_port
    options.add_argument('--proxy-server=http://'+proxy_ip_port+'')
    options.add_experimental_option('mobileEmulation', mobileEmulation)

    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
    # driver.get('https://brand.zzss.com/qunaweb/webview/xiangdao/index.html?sign=mnsw')

    driver.get('http://www.myylm.com')

    sleep(1)
    driver.close()


if __name__ == '__main__':
    for i in range(1,10):
        print i
        pv_()