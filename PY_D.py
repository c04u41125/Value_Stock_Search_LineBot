import pymysql

def table_exists(conn, userid):
    cursor = conn.cursor()
    sql = "SHOW TABLES LIKE '%s'" % userid
    cursor.execute(sql)
    return cursor.fetchone() is not None

def SAVE_info(userid, code, ans):
    db_setting = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "",
        "password": "",
        "db": "stocksearchtest",
        "charset": "utf8"
    }
    conn = pymysql.connect(**db_setting)

    try:
        with conn.cursor() as cursor:
            if table_exists(conn, userid):
                table_name = userid
                column_exists_query = f"SHOW COLUMNS FROM {table_name} LIKE '{code}'"
                cursor.execute(column_exists_query)

                # 獲取查詢結果
                columns = cursor.fetchall()

                # 檢查是否有找到欄位
                if columns:
                    # 欄位存在，不需創建
                    data_stock = (ans,)  # 將 ans 放入元組中
                    command = "INSERT INTO `{}` (`{}`) VALUES (%s)".format(userid, code)
                    cursor.execute(command, data_stock)
                    print('ok')
                else:
                    # 欄位不存在，創建新的欄位
                    alter_query = "ALTER TABLE `{}` ADD COLUMN `{}` VARCHAR(500)".format(userid, code)
                    cursor.execute(alter_query)
                    data_stock = (ans,)  # 將 ans 放入元組中
                    command = "INSERT INTO `{}` (`{}`) VALUES (%s)".format(userid, code)
                    cursor.execute(command, data_stock)
                    print('ok')

            else:
                create_table_query = '''
                CREATE TABLE `{}` (
                `{}` VARCHAR(6553))
                '''.format(userid, code)
                data_stock = [(ans,)]
                cursor.execute(create_table_query)
                command = "INSERT INTO `{}` (`{}`) VALUES (%s)".format(userid, code)

                cursor.execute(command, data_stock)
                print('ok')

        # 提交變更到資料庫
        conn.commit()

    finally:
        conn.close()

# 使用範例
# userid = input("請輸入代號: ")
# code = input("請輸入欄位名稱: ")
# ans = input("請輸入要插入的值: ")
# load_info(userid, code, ans)
