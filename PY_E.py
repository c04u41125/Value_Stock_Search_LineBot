import pymysql
import pandas as pd
from flask import send_file
from quickstart import to_drive
def LOAD_info(userid):

    db_setting = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "",
        "password": "",
        "db": "stocksearchtest",
        "charset": "utf8"
    }

    # 資料名稱
    table_name = userid

    conn = pymysql.connect(**db_setting)

    # 讀取資料到DataFrame
    query = "SELECT * FROM " + table_name
    df = pd.read_sql(query, conn)
    excel_file_path = "C:/testtest/Pocket_List.xlsx"  # Excel文件保存路徑

    df.to_excel(excel_file_path, sheet_name='STOCK', index=False)

    # 關閉mysql連結
    conn.close()

    # 轉譯成excel
    excel_file = "output"+userid+".xlsx"  # 輸出的文件名稱
    sheet_name = "Stock"
    df.to_excel(excel_file, sheet_name=sheet_name, index=False)
    print("已成功轉譯成excel檔")
    download_url=to_drive(userid)
    return download_url
    # print(download_url)
# LOAD_info('u2860badc047281e1fea8e449ce3569b4')
