from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
def DB_GET(code):
    #建立連結
    uri = "mongodb+srv://account:password@stocksearch.38esz2g.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    #設定資料庫
    db = client.stock
    col = db.stockdata
    #讀取資料
    result=col.find_one({'股票代碼':code})
    info=(f"股票名稱: {result['股票名稱']}\n"
    f"股票代碼: {result['股票代碼']}\n"
    f"{result['所屬年度1']}  :  股利 {result['總股利1']}  /  現金殖利率: {result['現金殖利率1']}\n"
    f"{result['所屬年度2']}  :  股利 {result['總股利2']}  /  現金殖利率: {result['現金殖利率2']}\n"
    f"{result['所屬年度3']}  :  股利 {result['總股利3']}  /  現金殖利率: {result['現金殖利率3']}\n"
    f"{result['所屬年度4']}  :  股利 {result['總股利4']}  /  現金殖利率: {result['現金殖利率4']}\n"
    f"{result['所屬年度5']}  :  股利 {result['總股利5']}  /  現金殖利率: {result['現金殖利率5']}\n"
    f"{result['時間1']}  :  EPS: {result['EPS1']}  /  營收年增率: {result['營收年增率1']}\n"
    f"{result['時間2']}  :  EPS: {result['EPS2']}  /  營收年增率: {result['營收年增率2']}\n"
    f"{result['時間3']}  :  EPS: {result['EPS3']}  /  營收年增率: {result['營收年增率3']}\n"
    f"{result['時間4']}  :  EPS: {result['EPS4']}  /  營收年增率: {result['營收年增率4']}\n"
    f"{result['時間5']}  :  EPS: {result['EPS5']}  /  營收年增率: {result['營收年增率5']}\n"
    f"建議合理價: {result['合理股價']} ")
    return info
#     print(info)
# DB_GET('2330')
