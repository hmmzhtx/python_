# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re


def detect_landline(landline_number):
    if landline_number[0:1] == '1':
        return False
    else:
        return True


# 凡是出现sleep的，都是因为网络等原因加载过慢，需要等一等
def extract(driver, v_num, v_companyName):
    handles = driver.window_handles
    driver.switch_to_window(handles[0])
    try:
        company_input = driver.find_elements_by_tag_name("input")[0]
        company_input.clear()
        company_input.clear()
        va = v_companyName
        vva = va.decode('utf-8')
        company_input.send_keys(vva)
        getButton = driver.find_element_by_class_name("search-btn")
        getButton.click()
        time.sleep(3)
        try:
            select_company = driver.find_element_by_link_text(v_companyName)
            select_company.click()
            time.sleep(3)
            handles = driver.window_handles
            driver.switch_to_window(handles[1])
            falseTrue = driver.find_element_by_xpath('//*[@id="homeMainContent"]/div/div[1]/div/div/div[1]/div/span').text
            resultVa = ''
            if falseTrue == u'您已添加该线索':
                resultVa = "已经添加"
                driver.close()
            elif falseTrue == u'请选择联系方式，添加为我的线索':
                time.sleep(2)
                getEye_txt = driver.find_element_by_xpath('//*[@id="report"]/div[1]/div/div/div/div/div[3]/span').text
                if getEye_txt ==  u'点击查看':
                    getButton = driver.find_element_by_xpath('//*[@id="report"]/div[1]/div/div/div/div/div[3]')
                    getButton.click()
                    time.sleep(1)

                no_Txt = driver.find_element_by_xpath('//*[@id="report"]/div[1]/div/div/div[1]/div[1]/div/span[2]').text
                if no_Txt == '0':
                    resultVa = "无联系方式"
                    driver.close()
                    time.sleep(3)
                else:
                    select_txt = driver.find_element_by_xpath('//*[@id="report"]/div[1]/div/div/div[2]/div/div[1]/ul/div/div/div[1]/div/div/div[1]/div[1]/div[2]/div/a').text
                    falgPhone = detect_landline(select_txt)
                    if falgPhone:
                        resultVa = "座机号"
                        driver.close()
                        time.sleep(3)
                    else:
                        selectdir = driver.find_element_by_xpath('//*[@id="report"]/div[1]/div/div/div[2]/div/div[1]/ul/div/div/div[1]/div/div/div[1]/div[3]/div[3]')
                        selectdir.click()
                        time.sleep(2)
                        selectdir = driver.find_element_by_xpath('//*[@id="report"]/div[1]/div/div/div[2]/div/div[1]/ul/div/div/div[1]/div/div/div[2]/div[2]')
                        selectdir.click()
                        time.sleep(3)
                        resultVa = "处理完成"
                        driver.close()
                        time.sleep(3)
        except NoSuchElementException:
            resultVa = "在第一页无查询到"
    except NoSuchElementException:
        resultVa = "没法识别"
        pass
    rrv = v_num + '#' + v_companyName + '#' + resultVa
    print rrv
    # 源文件处理结果路径
    pathOne = "C:\\work\\2.txt"
    uipathOne = unicode(pathOne, "utf8")
    fileOne = open(uipathOne, "a")
    fileOne.write(rrv)
    fileOne.write('\n')


def read_txt(filepath):
    file = open(filepath, 'r')
    fl = file.readlines()
    num = []
    companyNameList = []
    for x in fl:
        url_pass = x.strip()  # 除去每行的换行符
        if url_pass.find(',')> 0:
            url_pass_str =  url_pass.split(',')
            num.append(url_pass_str[0])
            companyNameList.append(url_pass_str[1])
    return num, companyNameList


# 调用执行
def doWork():
    # # 设置代理
    # PROXY = "123.169.103.4:4145"
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
    # # 一定要注意，=两边不能有空格，不能是这样--proxy-server = 202.20.16.82:10152
    # driver = webdriver.Chrome(chrome_options = chrome_options)
    # # driver.get("http://httpbin.org/ip")
    # # print(driver.page_source)
    # # driver.quit()
    driver = webdriver.Chrome()
    #必须进行自身登陆后，在元素中获取 ifram 框架的链接，这样不用再次进行登录操作
    driver.get( 'http://yqx.finndy.com/login?access_token=Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDg4OTVhZDE2YzhhYzMzN2FkN2FhZDIiLCJyb2xlIjoibWFpbmFjY291bnQiLCJzZXF1ZW5jZSI6MCwic3RhdHVzIjoxLCJkaXNhYmxlIjpmYWxzZSwiaWF0IjoxNTcyNjg0NzA5LCJleHAiOjE1NzI3NDIzMDl9.hMtIyXc6J4AZTuaCRVE3WHjZQFYkPtrSuxF8k80mTkQ&redirect=%2fsearch')
    time.sleep(5)
    # 源文件处理路径
    filepath = 'C:\\work\\98_1.txt'
    num, companyNameList = read_txt(filepath)
    for index in range(len(companyNameList)):
        v_num = num[index]
        v_companyName = companyNameList[index]
        # time.sleep(3)
        extract(driver, v_num, v_companyName)
    driver.quit()

def porxy():
    # 设置代理
    PROXY = "178.128.243.130:8080"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = 202.20.16.82:10152
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://httpbin.org/ip")
    print(driver.page_source)
    driver.quit()

if __name__ == '__main__':
    # porxy()
    doWork()