# -*- coding:utf-8 -*-


# sheet_name：返回指定的sheet，如果将sheet_name指定为None，则返回全表，如果需要返回多个表，可以将sheet_name指定为一个列表，例如['sheet1', 'sheet2']
# header：指定数据表的表头，默认值为0，即将第一行作为表头。
# usecols：读取指定的列，例如想要读取第一列和第二列数据：pd.read_excel("example.xlsx", sheet_name=None, usecols=[0, 1])
# onverters={'col1', func} 对选定列使用函数func转换，通常表示编号的列会使用（避免转换成int）

import numpy as np
import pandas as pd
from model.mysql.LocalMysqlTest import LocalMysqlTest

np.set_printoptions(suppress=True)

def import_zzss_successdata_info():
    localTestMysql.executeSqlByEngine("delete from  zzss_successdata_info;")

    file = r'C:\Users\huangmingming\Desktop\1.xlsx'
    file = unicode(file, "utf8")
    df = pd.read_excel(file, sheet_name=["2014-2019"], usecols=[1, 2, 3, 4, 5, 6, 7, 8])
    cols = ["city", "date", "proName", "num", "pfT", "proNum", "specifications", "company"]
    for k, v in df.items():
        v.columns = cols
        v["city"] = v["city"]
        v['date'] = v['date'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
        v['proName'] = v["proName"]
        v['num'] = v["num"]
        v['pfT'] = v["pfT"]
        v['proNum'] = v["proNum"]
        v['specifications'] = v["specifications"]
        v['company'] = v["company"]
        print v

        localTestMysql.save_DataFrame_PD(v, "zzss_successdata_info")


if __name__ == '__main__':
    localTestMysql = LocalMysqlTest(schema='20180527')
    import_zzss_successdata_info()