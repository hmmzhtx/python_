# -*- coding:utf-8 -*-


# sheet_name：返回指定的sheet，如果将sheet_name指定为None，则返回全表，如果需要返回多个表，可以将sheet_name指定为一个列表，例如['sheet1', 'sheet2']
# header：指定数据表的表头，默认值为0，即将第一行作为表头。
# usecols：读取指定的列，例如想要读取第一列和第二列数据：pd.read_excel("example.xlsx", sheet_name=None, usecols=[0, 1])
# onverters={'col1', func} 对选定列使用函数func转换，通常表示编号的列会使用（避免转换成int）

import numpy as np
import pandas as pd
from model.mysql.LocalMysqlTest import LocalMysqlTest
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

np.set_printoptions(suppress=True)

def import_machine_month_num():
    localTestMysql.executeSqlByEngine("delete from  machine_month_num;")
    file = r'D:\IPO新\2018\To黄明明\eric\机器上下线清单\【内部】机器点位清单20191204-Eric-20191128-V15.xlsx'
    file = unicode(file, "utf8")
    df = pd.read_excel(file, sheet_name=[r"数据库的点位数据"])
    cols = ["sid", "mac_no", "mac_name", "city", "mac_up_name", "ct", "et", "rsn", "srp_rsn", "prop", "up_prop", "abc", "mtype", "cms_online", "cms_exit", "city_leve", "address", "remark", "original_ct"]
    for k, v in df.items():
        v.columns = cols
        v["sid"] = v["sid"]
        v['mac_no'] = v["mac_no"]
        v['mac_name'] = v["mac_name"]
        v['city'] = v["city"]
        v['mac_up_name'] = v["mac_up_name"]
        v['ct'] = v["ct"]
        v['et'] = v["et"]
        v['rsn'] = v["rsn"]
        v['srp_rsn'] = v["srp_rsn"]
        v['prop'] = v["prop"]
        v['up_prop'] = v["up_prop"]
        v['abc'] = v["abc"]
        v['mtype'] = v["mtype"]
        v['cms_online'] = v["cms_online"]
        v['cms_exit'] = v["cms_exit"]
        v['city_leve'] = v["city_leve"]
        v['address'] = v["address"]
        v['remark'] = v["remark"]
        v['original_ct'] = v["original_ct"]
        localTestMysql.save_DataFrame_PD(v, "machine_month_num")


if __name__ == '__main__':
    month_arr = [
        ['01', '1141', '2019-01-31 23:59:59', '2019-02-01 00:00:00'],
        ['02', '1172', '2019-02-28 23:59:59', '2019-03-01 00:00:00'],
        ['03', '1372', '2019-03-31 23:59:59', '2019-04-01 00:00:00'],
        ['04', '1535', '2019-04-30 23:59:59', '2019-05-01 00:00:00'],
        ['05', '1716', '2019-05-31 23:59:59', '2019-06-01 00:00:00'],
        ['06', '1961', '2019-06-30 23:59:59', '2019-07-01 00:00:00'],
        ['07', '2249', '2019-07-31 23:59:59', '2019-08-01 00:00:00'],
        ['08', '2584', '2019-08-31 23:59:59', '2019-09-01 00:00:00'],
        ['09', '2978', '2019-09-30 23:59:59', '2019-10-01 00:00:00'],
        ['10', '3200', '2019-10-31 23:59:59', '2019-11-01 00:00:00'],
        ['11', '3600', '2019-11-30 23:59:59', '2019-12-01 00:00:00'],
        ['12', '4000', '2019-12-31 23:59:59', '2020-01-01 00:00:00'],
    ]


    localTestMysql = LocalMysqlTest(schema='test')
    import_machine_month_num()
    for ar in month_arr:
        month = ar[0]
        to_num = ar[1]
        ct = ar[2]
        et = ar[3]
        sql = "SELECT count(1) as 'num' from  machine_month_num where ct <= '{}' and et >= '{}';".format(ct,et)
        month_num = localTestMysql.get_DataFrame_PD(sql)
        num = month_num['num'][0]
        c_num = int(to_num) - int(num)
        print "sql：{},月份：{},目标量：{},点位量：{},差：{}".format(sql,month,to_num,num,c_num)