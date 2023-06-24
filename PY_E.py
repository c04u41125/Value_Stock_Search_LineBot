import pymysql
import pandas as pd
from flask import send_file
from quickstart import to_drive
def LOAD_info(userid):

    db_setting = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "821012",
        "db": "stocksearchtest",
        "charset": "utf8"
    }

    # 资料表名称
    table_name = userid

    conn = pymysql.connect(**db_setting)

    # 读取资料表资料到DataFrame
    query = "SELECT * FROM " + table_name
    df = pd.read_sql(query, conn)
    excel_file_path = "C:/testtest/Pocket_List.xlsx"  # Excel文件保存的路径

    df.to_excel(excel_file_path, sheet_name='STOCK', index=False)

    # 关闭MySQL连接
    conn.close()

    # 写入Excel文件
    excel_file = "output"+userid+".xlsx"  # 输出的Excel文件名称
    sheet_name = "Stock"
    df.to_excel(excel_file, sheet_name=sheet_name, index=False)
    print("数据已成功写入Excel文件")
    download_url=to_drive(userid)
    return download_url
    # print(download_url)
# LOAD_info('u2860badc047281e1fea8e449ce3569b4')
