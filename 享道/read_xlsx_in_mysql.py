# -*- coding:utf-8 -*-
# sheet_name：返回指定的sheet，如果将sheet_name指定为None，则返回全表，如果需要返回多个表，可以将sheet_name指定为一个列表，例如['sheet1', 'sheet2']
# header：指定数据表的表头，默认值为0，即将第一行作为表头。
# usecols：读取指定的列，例如想要读取第一列和第二列数据：pd.read_excel("example.xlsx", sheet_name=None, usecols=[0, 1])
# onverters={'col1', func} 对选定列使用函数func转换，通常表示编号的列会使用（避免转换成int）


import pandas as pd
from model.mysql.LocalMysqlTest import LocalMysqlTest
import sys
import numpy as np
import os
reload(sys)
sys.setdefaultencoding("utf-8")

np.set_printoptions(suppress=True)

# 列出文件夹下所有的目录与文件
def list_all_files(rootdir):
    _files = []
    list = os.listdir(unicode(rootdir, "utf8"))  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir+r'\\', list[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files



def import_xiangdao():
    localTestMysql.executeSqlByEngine("delete from  xiangdao;")

    file_date_dir = os.path.join(r"C:\Users\huangmingming\Desktop", '产品结案数据','享道', '麦客')  # 日期文件夹

    _files = list_all_files(file_date_dir)
    for i in range(0, len(_files)):
        filePath = _files[i]
        fileNameType = os.path.basename(filePath)
        file_name = fileNameType.split('.')[0]
        city = file_name.split('-')[0]

        print(filePath)
        # file = unicode(filePath, "utf8")
        df = pd.read_excel(filePath, sheet_name=["Sheet1"], header=2, usecols=[0, 1, 2, 3, 4])
        cols = ["num", "d_one", "d_two", "phone_one", "phone_two"]
        for k, v in df.items():
            v.columns = cols
            v["file_name"] = file_name
            v['city'] = city
            v['d_one'] = v["d_one"] # .apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
            v['d_two'] = v["d_two"]
            v['phone_one'] = v["phone_one"]
            v['phone_two'] = v["phone_two"]
            localTestMysql.save_DataFrame_PD(v, "xiangdao")
        localTestMysql.executeSqlByEngine("UPDATE xiangdao set d_two = left(d_one,10);")
        localTestMysql.executeSqlByEngine("DELETE from xiangdao where  (num REGEXP '[^0-9.]') != 0 or num is null;")
        localTestMysql.executeSqlByEngine("UPDATE xiangdao set phone_one = phone_two WHERE phone_two REGEXP '[1][356789][0-9]{9}';")




        # localTestMysql.executeSqlByEngine("UPDATE tamll_u set ymd = left(crtime,10);")
        # localTestMysql.executeSqlByEngine("update tamll_u a set a.channel = (select  b.channel from tmall_config b where b.channelID = a.channelID);")
        # localTestMysql.executeSqlByEngine("update tamll_u a set a.channelname = (select  b.channelname from tmall_config b where b.channelID = a.channelID);")


if __name__ == '__main__':
    localTestMysql = LocalMysqlTest(schema='test')
    import_xiangdao()
    # date = '2019-12-20'
    # last_time = localTestMysql.get_DataFrame_PD("SELECT max(crtime) as 'time' from tamll_u where ymd = '{}';".format(date))
    # print u'统计截至日期：'+ last_time['time'][0]
    # df = localTestMysql.get_DataFrame_PD("SELECT channel,ymd,proname,count(DISTINCT taobaoID) as 'num' from tamll_u where ymd = '{}' GROUP BY channel,ymd,proname;".format(date))
    # for index, row in df.iterrows():
    #     print row['channel'] + ',' + row['ymd'] + ',' + row['proname'] + ',' + str(row['num'])
    #


