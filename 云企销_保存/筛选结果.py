# -*- coding:utf-8 -*-


# sheet_name：返回指定的sheet，如果将sheet_name指定为None，则返回全表，如果需要返回多个表，可以将sheet_name指定为一个列表，例如['sheet1', 'sheet2']
# header：指定数据表的表头，默认值为0，即将第一行作为表头。
# usecols：读取指定的列，例如想要读取第一列和第二列数据：pd.read_excel("example.xlsx", sheet_name=None, usecols=[0, 1])
# onverters={'col1', func} 对选定列使用函数func转换，通常表示编号的列会使用（避免转换成int）

import numpy as np
import pandas as pd
from model.mysql.LocalMysqlTest import LocalMysqlTest

np.set_printoptions(suppress=True)

def import_yxq():
    localTestMysql.executeSqlByEngine("delete from  yqx where ty = '"+ty+"';")
    file = r'C:\Users\huangmingming\Desktop\2.xlsx'
    file = unicode(file, "utf8")
    df = pd.read_excel(file, header=2, sheet_name=["Sheet1"], usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13])
    cols = ["num", "add_date", "company", "name", "mobile","fixed_line","email","qq","comfrom","legal_person","established","registered_capital","registered_address","remark"]
    for k, v in df.items():
        v.columns = cols
        v["num"] = v["num"]
        v['add_date'] = v["add_date"]
        v['company'] = v["company"]
        v['name'] = v["name"]
        v['mobile'] = v["mobile"]
        v['fixed_line'] = v["fixed_line"]
        v['email'] = v["email"]
        v['qq'] = v["qq"]
        v['comfrom'] = v["comfrom"]
        v['legal_person'] = v["legal_person"]
        v['established'] = v["established"]
        v['registered_capital'] = v["registered_capital"]
        v['registered_address'] = v["registered_address"]
        v['remark'] = v["remark"]
        v['ty'] = ty
        # print v
        localTestMysql.save_DataFrame_PD(v, "yqx")

def remobile_num(mobile_num):
    if  mobile_num >= 30:
        return 8
    elif  mobile_num >= 15:
        return 6
    elif  mobile_num >= 8:
        return 4
    elif  mobile_num >= 3:
        return 3
    else:
        return 3





if __name__ == '__main__':

    ty = '6'
    localTestMysql = LocalMysqlTest(schema='test')
    import_yxq()
    df = localTestMysql.get_DataFrame_PD("select  company,count(1) as mobile_num from  yqx where mobile is not null and ty = '"+ty+"' GROUP BY company;")
    for index, row in df.iterrows():
        company = row['company']
        mobile_num = row['mobile_num']
        n = remobile_num(mobile_num)
        # print row['company'], n
        re_df = localTestMysql.get_DataFrame_PD("select name,mobile,company,email from yqx  where mobile is not null and ty = '"+ty+"' and  company = '"+company+"' limit "+str(n)+";")
        # re_df.to_excel("C:\\work\\111.xlsx",index = False)
        for index,row in re_df.iterrows():
            name = row['name']
            mobile = row['mobile']
            company = row['company']
            email = row['email']

            if name is not None:
                name = name
            else:
                name = u''

            if mobile is not None:
                mobile = mobile
            else:
                mobile = u''

            if company is not None:
                company = company
            else:
                company = u''

            if email is not None:
                email = email
            else:
                email = u''

            print u'展会' + ',' +   name + ',' +  str(mobile) + ',' +  company + ',' + email
            result = u'展会' + ',' +   name + ',' +  mobile + ',' +  company + ',' + email
            # result = str('展会') + ',' + str(name) + ',' + str(mobile) + ',' + str(company) + ',' + str(email)
            # 源文件处理结果路径
            pathOne = "C:\\work\\222.csv"
            uipathOne = unicode(pathOne, "utf8")
            fileOne = open(uipathOne, "a")
            fileOne.write(unicode.encode(result,'utf-8'))
            fileOne.write('\n')




