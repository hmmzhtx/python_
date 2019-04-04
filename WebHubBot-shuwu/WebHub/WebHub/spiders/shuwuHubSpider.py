#coding:utf-8
import logging
import datetime
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request


# # 列出文件夹下所有的目录与文件
# def list_all_files(rootdir):
#     import os
#     _files = []
#     list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
#     for i in range(0, len(list)):
#         path = os.path.join(rootdir, list[i])
#         if os.path.isdir(path):
#             _files.extend(list_all_files(path))
#         if os.path.isfile(path):
#             _files.append(path)
#     return _files


class Spider(CrawlSpider):
    name = 'shuwuHubSpider'
    host = 'http://www.shuwu.mobi'

    logging.getLogger("requests").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='cataline.log',
        filemode='w')

    ## 爬取前面2页-查看是否为当天发布   目录文章连接
    def start_requests(self):
        for num in range(1, 2):
            yield Request(url='http://www.shuwu.mobi/page/%s' % num, callback=self.parse_ph_info)

    def parse_ph_info(self, response):
        selector = Selector(response)
        logging.debug('request url:------>' + response.url)
        divs = selector.xpath('//*[@id="primary"]/ul/li')

        for div in divs:
            book_type_a = div.xpath('div[1]/div[1]/a')
            a_all_txt = ''
            for a_a in book_type_a:
                book_type_txt = a_a.xpath('text()').extract()[0]
                a_all_txt = a_all_txt + '-' + book_type_txt

            url = div.xpath('div[2]/h2/a/@href').extract()
            url_txt = url[0]

            date = div.xpath('div[2]/div/text()').extract()[0].strip()[0:10].replace('.','-')
            old_date = str(date)
            now_date = datetime.datetime.now().strftime('%Y-%m-%d')
            if old_date == now_date:
                print a_all_txt ##文本名称
                ss = url_txt.split('/')  # 文本分割，以table键分割
                n = len(ss)
                start_atr = ss[n - 1]
                start_atr_new = start_atr.replace('.html', '').replace('\n', '')
                print start_atr_new
                yield Request(url='http://www.shuwu.mobi/download.php?id=' + start_atr_new.encode("utf-8").strip(),meta={'item': a_all_txt}, callback=self.parse_baidu_info)

    def parse_baidu_info(self, response):
        txt_value = response.meta['item']
        selector = Selector(response)
        logging.debug('request url:------>' + response.url)
        div_baidu = selector.xpath('/html/body/div[5]/a[1]/@href').extract()
        baidu = div_baidu[0]

        div_baidu_pass = selector.xpath('/html/body/div[3]/p[6]/text()').extract()
        baidu_pass = div_baidu_pass[0]
        baidu_pass_new = baidu_pass[12:16]

        pathOne = 'C:\\work\\小书屋\\'
        uipathOne = unicode(pathOne, "utf8")
        fileOne = open(uipathOne + txt_value + '.txt', "a")
        fileOne.write(baidu + '#' + baidu_pass_new)
        fileOne.write('\n')


    # ## 爬取前面2页-查看是否为当天发布   目录文章连接
    # def start_requests(self):
    #     for num in range(1, 2):
    #         yield Request(url='http://www.shuwu.mobi/page/%s' % num, callback=self.parse_ph_info)
    #
    # def parse_ph_info(self, response):
    #     phItem = PornVideoItem()
    #     selector = Selector(response)
    #     logging.debug('request url:------>' + response.url)
    #     divs = selector.xpath('//*[@id="primary"]/ul/li')
    #
    #     for div in divs:
    #         book_type_a = div.xpath('div[1]/div[1]/a')
    #         a_all_txt = ''
    #         for a_a in book_type_a:
    #             book_type_txt = a_a.xpath('text()').extract()[0]
    #             a_all_txt = a_all_txt + '-' + book_type_txt
    #
    #         url = div.xpath('div[2]/h2/a/@href').extract()
    #         url_txt = url[0]
    #
    #         date = div.xpath('div[2]/div/text()').extract()[0].strip()[0:10].replace('.','-')
    #         old_date = str(date)
    #         now_date = datetime.datetime.now().strftime('%Y-%m-%d')
    #         if old_date == now_date:
    #             print a_all_txt
    #             pathOne = "C:\\work\\"+a_all_txt+".txt"
    #             fileOne = open(pathOne, "a")
    #             fileOne.write(url_txt)
    #             fileOne.write('\n')
    #     yield phItem
    # ## 爬取前面2页-查看是否为当天发布   目录文章连接

    # ## 爬取二级目录文章连接
    # def start_requests(self):
    #     name = 'jxks'
    #     yield Request(url='http://www.shuwu.mobi/category/gjs/'+name+'', callback=self.parse_ph_info)
    #     for num in range(2,2):
    #          yield Request(url='http://www.shuwu.mobi/category/gjs/'+name+'/page/%s'% num ,callback=self.parse_ph_info)
    #
    # def parse_ph_info(self, response):
    #     phItem = PornVideoItem()
    #     selector = Selector(response)
    #     logging.debug('request url:------>' + response.url)
    #     divs = selector.xpath('//*[@id="primary"]/ul/li')
    #
    #     for div in divs:
    #         url = div.xpath('div/h2/a/@href').extract()
    #         print url[0]
    #         pathOne = "C:\\work\\教学考试.txt"
    #         uipathOne = unicode(pathOne, "utf8")
    #         fileOne = open(uipathOne, "a")
    #         fileOne.write(url[0])
    #         fileOne.write('\n')
    #     yield phItem
    # ## 爬取二级目录文章连接


    # ## 爬取文章下载
    # def start_requests(self):
    #     filepath = 'C:\\work\\小书屋\\编号'
    #     filepath = unicode(filepath, "utf-8")
    #     files = list_all_files(filepath)
    #     for item in files:
    #         txt_value = item.split('\\')[4]  # 文本分割，以table键分割
    #
    #         bashPath = u'' + item + ''
    #         file = open(bashPath, 'r')
    #         fl = file.readlines()
    #         for x in fl:
    #             url = x.strip()  # 除去每行的换行符
    #             yield Request(url = url, meta={'item': txt_value}, callback=self.parse_ph_info)
    #
    # def parse_ph_info(self, response):
    #     txt_value = response.meta['item']
    #     phItem = PornVideoItem()
    #     selector = Selector(response)
    #     logging.debug('request url:------>' + response.url)
    #     div_baidu = selector.xpath('/html/body/div[5]/a[1]/@href').extract()
    #     baidu = div_baidu[0]
    #
    #     div_baidu_pass = selector.xpath('/html/body/div[3]/p[6]/text()').extract()
    #     baidu_pass = div_baidu_pass[0]
    #     baidu_pass_new = baidu_pass[12:16]
    #
    #     pathOne = 'C:\\work\\小书屋\\百度\\'
    #     uipathOne = unicode(pathOne, "utf8")
    #     fileOne = open(uipathOne + txt_value, "a")
    #     fileOne.write(baidu + '#' + baidu_pass_new)
    #     fileOne.write('\n')
    #
    #     yield phItem
    # ## 爬取文章下载
