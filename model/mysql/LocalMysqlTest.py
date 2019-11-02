# -*-coding: utf-8-*-
import logging
import sys
import traceback
from itertools import cycle

import pandas as pd
from sqlalchemy import create_engine
import decimal

class LocalMysqlTest(object):
    # 初始化
    def __init__(self,schema='test'):
        self._engin = create_engine('mysql+pymysql://root:root@localhost:3306/'+schema+'?charset=utf8mb4')

    # 连接池状态
    def getPoolStatus(self):
        return self._engin.pool.status()

    # 获取连接
    def getConnection(self):
        conn = self._engin.connect()
        # logging.info(self._engin.pool.status())
        # print("=======")
        return conn

    # 释放连接
    def closeConnection(self, conn):
        if conn:
            conn.close()
            # print(self._engin.pool.status())
            # print("********")

    # 执行sql
    def executeSqlByEngine(self, sql='SELECT * FROM DUAL'):
        return self._engin.execute(sql)

    # 执行sql
    def executeSqlByConn(self, sql='SELECT * FROM DUAL', conn=None):
        conn = conn or self.getConnection()
        with conn as connection:
            return connection.execute(sql)

    # 批量执行更新sql语句
    def executeSqlManyByConn(self, sql='',data=[], conn=None):
        if len(data) >0 :
            conn = conn or self.getConnection()
            with conn as connection:
                return connection.execute(sql,data)

    # 加载数据到df(自定义索引) 不推荐
    def load_DataFrame_Conn(self, sql='SELECT * FROM DUAL', conn=None):
        conn = conn or self.getConnection()
        with conn as connection:
            dataList = list(connection.execute(sql))
            dataFrame = pd.DataFrame(dataList, index=[(n + 1) for n in range(len(dataList))])
            return dataFrame

    # 加载数据到df 不推荐
    def get_DataFrame_Conn(self, sql='SELECT * FROM DUAL', conn=None):
        conn = conn or self.getConnection()
        with conn as connection:
            dataList = list(connection.execute(sql))
            dataFrame = pd.DataFrame(dataList)
            return dataFrame

    # 加载数据到df
    def get_DataFrame_PD(self, sql='SELECT * FROM DUAL', conn=None):
        conn = conn or self.getConnection()
        with conn as connection:
            dataFrame = pd.read_sql(sql, connection)
            return dataFrame

    # 保存df到数据库
    def save_DataFrame_PD(self, pd, table, conn=None):
        conn = conn or self.getConnection()
        with conn as connection:
            pd.to_sql(table, connection, if_exists='append', index=False)


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        stream=sys.stdout,
                        filemode='a+')

    try:
        qunaMysql = LocalMysqlTest()


    except:
        ex = traceback.format_exc()
        logging.error(ex)
    finally:
        print(qunaMysql._engin.pool.status())
        # print(qunaMysql._engin.pool.checkedin())
        # print(qunaMysql._engin.pool.checkedout())
        pass
