# -*- coding:utf-8 -*-


# sheet_name：返回指定的sheet，如果将sheet_name指定为None，则返回全表，如果需要返回多个表，可以将sheet_name指定为一个列表，例如['sheet1', 'sheet2']
# header：指定数据表的表头，默认值为0，即将第一行作为表头。
# usecols：读取指定的列，例如想要读取第一列和第二列数据：pd.read_excel("example.xlsx", sheet_name=None, usecols=[0, 1])
# onverters={'col1', func} 对选定列使用函数func转换，通常表示编号的列会使用（避免转换成int）

import numpy as np
import pandas as pd
from model.mysql.LocalMysqlTest import LocalMysqlTest

np.set_printoptions(suppress=True)

def import_tmall_u():
    localTestMysql.executeSqlByEngine("delete from  tamll_u;")
    file = r'C:\Users\huangmingming\Desktop\测试.xlsx'
    file = unicode(file, "utf8")
    df = pd.read_excel(file, sheet_name=["Sheet1"], usecols=[1, 2, 6, 9, 13])
    cols = ["channelID", "nickname", "proname", "taobaoID", "crtime"]
    for k, v in df.items():
        v.columns = cols
        v["channelID"] = v["channelID"]
        v['nickname'] = v["nickname"]
        v['proname'] = v["proname"]
        v['taobaoID'] = v["taobaoID"]
        v['crtime'] = v['crtime'].apply(lambda x: x.strftime('%Y-%m-%d'))
        # print v
        localTestMysql.save_DataFrame_PD(v, "tamll_u")
    localTestMysql.executeSqlByEngine("UPDATE tamll_u set ymd = left(crtime,10);")
    localTestMysql.executeSqlByEngine("update tamll_u a set a.channel = (select  b.channel from tmall_config b where b.channelID = a.channelID);")
    localTestMysql.executeSqlByEngine("update tamll_u a set a.channelname = (select  b.channelname from tmall_config b where b.channelID = a.channelID);")


if __name__ == '__main__':
    localTestMysql = LocalMysqlTest(schema='test')
    import_tmall_u()
    df = localTestMysql.get_DataFrame_PD("SELECT channel,ymd,proname,count(DISTINCT taobaoID) as 'num' from tamll_u where ymd = '2019-10-31' GROUP BY channel,ymd,proname;")
    print df
