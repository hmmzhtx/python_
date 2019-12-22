# -*- coding:utf-8 -*-
import json
import urllib, urllib2, base64
import os
access_token = '24.abcb6a51415e1c733d0bc4046ed9ce3b.2592000.1579056791.282335-17520392'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token
# url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
# 二进制方式打开图文件
for root,dirs,files in os.walk("d:\\pic\\1\\"):
    for file in files:
        path =  os.path.join(root,file).decode('gbk').encode('utf-8')
        f = open(r''+path+'', 'rb')
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = urllib.urlencode(params)
        request = urllib2.Request(url, params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if (content):
            print(content)
            jsonData = json.loads(content)
            for i in range(0,jsonData['words_result_num']):
                print path
                words = jsonData['words_result'][i]['words']
                print words
                result = path + '###' + words
                print result
                pathOne = "d:\\pic\\2017-06-16 2017上海国际营养健康产业展览会 2017上海国际有机食品和绿色食品博览会 2017上海国际休闲食品及进口食品博览会.txt"
                uipathOne = unicode(pathOne, "utf8")
                fileOne = open(uipathOne, "a")
                fileOne.write(result.encode("utf-8").strip())
                fileOne.write('\n')