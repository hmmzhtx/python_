# -*- coding: UTF-8 -*-
import xlrd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


# 凡是出现sleep的，都是因为网络等原因加载过慢，需要等一等

# 登录云盘
def login(driver, username, password):
    orgin_url = 'https://pan.baidu.com/'
    driver.get(orgin_url)
    time.sleep(10)
    elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    elem_static.click()
    time.sleep(10)
    elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    elem_username.clear()
    elem_username.send_keys(username)
    elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    elem_userpas.clear()
    elem_userpas.send_keys(password)
    elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    elem_submit.click()
    time.sleep(30)


# 将加密分享的文件保存到自己云盘的目录下[AA]
# txt_value  二级目录,是txt文件的文件名，需要自己在网盘中提前创建好
def extract(driver, srcurl, srcpwd, txt_value):
    driver.get(srcurl)
    try:
        getpwd = driver.find_element_by_id("hvje7l")
        getpwd.send_keys(srcpwd)
        getButton = driver.find_element_by_link_text("提取文件")
        getButton.click()
        time.sleep(5)
        # 目前有两种情况
        # 一：分享文件是一压缩包
        # 二：分享的是一路径
        try:
            # 全选（情况二）
            selectall = driver.find_element_by_class_name("zbyDdwb")
            selectall.click()
        except NoSuchElementException:
            file_name = "no_zbyDdwb.png"
            driver.save_screenshot(file_name)
            driver.get_screenshot_as_file(file_name)
            pass

        savetodisk = driver.find_element_by_link_text("保存到网盘")
        savetodisk.click()
        time.sleep(3)
        # AAAA 保存路径 --  只能到一级目录
        selectdir = driver.find_element_by_xpath("//span[@node-path='/A小书屋']")
        selectdir.click()
        time.sleep(3)

        pp = u"//span[@node-path='/A小书屋/"+ txt_value +"']"
        selectdir = driver.find_element_by_xpath(pp)
        selectdir.click()
        time.sleep(2)

        enter = driver.find_element_by_link_text("确定")
        enter.click()
        time.sleep(3)
    except NoSuchElementException:
        file_name = "no_such_element.png"
        driver.get_screenshot_as_file(file_name)
        pass


# 从txt中读取分享链接和提取密码（格式 链接#密码 ：http://*********.com#vkds）
def read_txt(filepath):
    # filepath = unicode(filepath, "utf-8")
    file = open(filepath, 'r')
    fl = file.readlines()
    listUrl = []
    listpwd = []
    for x in fl:
        url_pass = x.strip()  # 除去每行的换行符
        if url_pass.find('#')> 0:
            url_pass_str =  url_pass.split('#')
            listUrl.append(url_pass_str[0].encode('utf-8'))
            listpwd.append(url_pass_str[1].encode('utf-8'))
    return listUrl, listpwd


# 列出文件夹下所有的目录与文件
def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

def test_aa(txt_value):
    pp = u"//span[@node-path='/A小书屋/" + txt_value + "']"

# 调用执行
def doWork():
    driver = webdriver.Chrome()
    login(driver, u"梦魂ghost", "H0848203818h")


    filepath = 'C:\\work\\小书屋'
    filepath = unicode(filepath, "utf-8")
    files = list_all_files(filepath)
    for item in files:
        txt_value_arr = item.split('\\') # 文本分割，以table键分割
        txt_value = txt_value_arr[len(txt_value_arr) - 1].replace('.txt','')

        bashPath = r'' + item + ''
        listUrl, listpwd = read_txt(bashPath)
        for index in range(len(listUrl)):
            srcurl = listUrl[index]
            srcpwd = listpwd[index]
            print srcurl
            extract(driver, srcurl, srcpwd, txt_value)
            test_aa(txt_value)
    driver.quit()

if __name__ == '__main__':
    doWork()