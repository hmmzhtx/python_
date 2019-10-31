# -*- coding:utf-8 -*-
import json
import urllib, urllib2, base64
import os
access_token = '24.1d1da70e329993f61de65be1da1922ed.2592000.1573638228.282335-17520392'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token
# 二进制方式打开图文件
for root,dirs,files in os.walk("c:\\pic\\"):
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
                pathOne = "C:\\work\\company_53_1.txt"
                uipathOne = unicode(pathOne, "utf8")
                fileOne = open(uipathOne, "a")
                fileOne.write(result.encode("utf-8").strip())
                fileOne.write('\n')