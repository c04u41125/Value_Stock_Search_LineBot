import requests
import re
import stock_range
import openpyxl
import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://account:password@stocksearch.38esz2g.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.stock
col = db.stockdata

def search(): #所有要查詢變數與判斷式
    try:
        #-----總股利-----
        div_time_1=(js['data']['dividends'][0]['year']) #時間1
        if div_time_1 == str(time.localtime().tm_year-2):      #如果去年度無發放股利，所有資料往後遞延
            div_time_1='0'
            div_time_2=(js['data']['dividends'][0]['year'])
            div_time_3=(js['data']['dividends'][1]['year'])
            div_time_4=(js['data']['dividends'][2]['year'])
            div_time_5=(js['data']['dividends'][3]['year'])
            div_1='0'
            div_2=(js['data']['dividends'][0]['totalDividend'])
            div_3=(js['data']['dividends'][1]['totalDividend'])
            div_4=(js['data']['dividends'][2]['totalDividend'])
            div_5=(js['data']['dividends'][3]['totalDividend'])
        elif div_time_1 == str(time.localtime().tm_year):    #如果是季發放，所有資料新定義參數
            div_time_1=(js['data']['dividends'][1]['year'])
            div_time_2=(js['data']['dividends'][5]['year'])
            div_time_3=(js['data']['dividends'][9]['year'])
            div_time_4=(js['data']['dividends'][13]['year'])
            div_time_5=(js['data']['dividends'][17]['year'])
            d1=float(js['data']['dividends'][1]['totalDividend'])
            d2=float(js['data']['dividends'][2]['totalDividend'])
            d3=float(js['data']['dividends'][3]['totalDividend'])
            d4=float(js['data']['dividends'][4]['totalDividend'])
            d5=float(js['data']['dividends'][5]['totalDividend'])
            d6=float(js['data']['dividends'][6]['totalDividend'])
            d7=float(js['data']['dividends'][7]['totalDividend'])
            d8=float(js['data']['dividends'][8]['totalDividend'])
            d9=float(js['data']['dividends'][9]['totalDividend'])
            d10=float(js['data']['dividends'][10]['totalDividend'])
            d11=float(js['data']['dividends'][11]['totalDividend'])
            d12=float(js['data']['dividends'][12]['totalDividend'])
            d13=float(js['data']['dividends'][13]['totalDividend'])
            d14=float(js['data']['dividends'][14]['totalDividend'])
            d15=float(js['data']['dividends'][15]['totalDividend'])
            d16=float(js['data']['dividends'][16]['totalDividend'])
            div_1=(d1+d2+d3+d4)
            div_2=(d5+d6+d7+d8)
            div_3=(d9+d10+d11+d12)
            div_4=(d13+d14+d15+d16)
            div_5=(js['data']['dividends'][17]['totalDividend'])
        elif div_time_1 == str(time.localtime().tm_year-1):  #如果去年度時間值正確，所有資料如下定義
            div_time_1=(js['data']['dividends'][0]['year']) #時間1
            div_time_2=(js['data']['dividends'][1]['year']) #時間2
            div_time_3=(js['data']['dividends'][2]['year']) #時間3
            div_time_4=(js['data']['dividends'][3]['year']) #時間4
            div_time_5=(js['data']['dividends'][4]['year']) #時間5
            div_1=(js['data']['dividends'][0]['totalDividend']) #股利1
            div_2=(js['data']['dividends'][1]['totalDividend']) #股利2
            div_3=(js['data']['dividends'][2]['totalDividend']) #股利3
            div_4=(js['data']['dividends'][3]['totalDividend']) #股利4
            div_5=(js['data']['dividends'][4]['totalDividend']) #股利5
        DIV=[div_1,div_2,div_3,div_4,div_5]  #將股利加入LIST
        for x in range(len(DIV)):            #如果股利值為空值，帶入0
            if DIV[x]=='-':
                DIV[x] =0.0
            elif DIV[x] is not None :               
                DIV[x] = float(DIV[x])
            else:
                DIV[x] = 0.0
    except:                                  #沒有任何股利發放資料就給所有變數0
        div_time_1='0'
        div_time_2='0'
        div_time_3='0'
        div_time_4='0'
        div_time_5='0'
        div_1=0
        div_2=0
        div_3=0
        div_4=0
        div_5=0
        DIV=[div_1,div_2,div_3,div_4,div_5]
    #-----現金殖利率-----
    try:
        if div_time_1 == str(time.localtime().tm_year-2):      #如果去年度無發放股利，所有資料往後遞延
            yie_1='0'
            yie_2=(js['data']['dividends'][0]['ytmCashByExDate'])
            yie_3=(js['data']['dividends'][1]['ytmCashByExDate'])
            yie_4=(js['data']['dividends'][2]['ytmCashByExDate'])
            yie_5=(js['data']['dividends'][3]['ytmCashByExDate'])
        elif div_time_1 == str(time.localtime().tm_year):    #如果是季發放，所有資料新定義參數
            y1=float(js['data']['dividends'][1]['ytmCashByExDate'])
            y2=float(js['data']['dividends'][2]['ytmCashByExDate'])
            y3=float(js['data']['dividends'][3]['ytmCashByExDate'])
            y4=float(js['data']['dividends'][4]['ytmCashByExDate'])
            y5=float(js['data']['dividends'][5]['ytmCashByExDate'])
            y6=float(js['data']['dividends'][6]['ytmCashByExDate'])
            y7=float(js['data']['dividends'][7]['ytmCashByExDate'])
            y8=float(js['data']['dividends'][8]['ytmCashByExDate'])
            y9=float(js['data']['dividends'][9]['ytmCashByExDate'])
            y10=float(js['data']['dividends'][10]['ytmCashByExDate'])
            y11=float(js['data']['dividends'][11]['ytmCashByExDate'])
            y12=float(js['data']['dividends'][12]['ytmCashByExDate'])
            y13=float(js['data']['dividends'][13]['ytmCashByExDate'])
            y14=float(js['data']['dividends'][14]['ytmCashByExDate'])
            y15=float(js['data']['dividends'][15]['ytmCashByExDate'])
            y16=float(js['data']['dividends'][16]['ytmCashByExDate'])
            yie_1=(y1+y2+y3+y4)
            yie_2=(y5+y6+y7+y8)
            yie_3=(y9+y10+y11+y12)
            yie_4=(y13+y14+y15+y16)
            yie_5=(js['data']['dividends'][17]['ytmCashByExDate'])
        elif div_time_1 == str(time.localtime().tm_year-1):    #如果是去年度資料，所有資料為正確值
            yie_1=(js['data']['dividends'][0]['ytmCashByExDate']) #現金殖利率1
            yie_2=(js['data']['dividends'][1]['ytmCashByExDate']) #現金殖利率2
            yie_3=(js['data']['dividends'][2]['ytmCashByExDate']) #現金殖利率3
            yie_4=(js['data']['dividends'][3]['ytmCashByExDate']) #現金殖利率4
            yie_5=(js['data']['dividends'][4]['ytmCashByExDate']) #現金殖利率5
        YIE=[yie_1,yie_2,yie_3,yie_4,yie_5] #將現金殖利率加入LIST
        for x in range(len(YIE)):           #如果現金殖利率值為空值，帶入0
            if YIE[x]=='-':
                YIE[x]=0.0
            elif YIE[x] is not None:               
                YIE[x] = float(YIE[x])
            else:
                YIE[x] = 0.0
    except:                                 #沒有任何現金殖利率資料就給所有變數0
        yie_1=0
        yie_2=0
        yie_3=0
        yie_4=0
        yie_5=0
        YIE=[yie_1,yie_2,yie_3,yie_4,yie_5] #將現金殖利率加入LIST

    #-----EPS-----
    try:
        eps_time_1=(js_eps["data"]["data"]["result"]["revenues"][0]['date']).replace("+08:00", "")[:4] #時間1
        eps_time_2=(js_eps["data"]["data"]["result"]["revenues"][1]['date']).replace("+08:00", "")[:4] #時間2
        eps_time_3=(js_eps["data"]["data"]["result"]["revenues"][2]['date']).replace("+08:00", "")[:4] #時間3
        eps_time_4=(js_eps["data"]["data"]["result"]["revenues"][3]['date']).replace("+08:00", "")[:4] #時間4
        eps_time_5=(js_eps["data"]["data"]["result"]["revenues"][4]['date']).replace("+08:00", "")[:4] #時間5
        eps_1=(js_eps["data"]["data"]["result"]["revenues"][0]['eps']) #EPS1
        eps_2=(js_eps["data"]["data"]["result"]["revenues"][1]['eps']) #EPS2
        eps_3=(js_eps["data"]["data"]["result"]["revenues"][2]['eps']) #EPS3
        eps_4=(js_eps["data"]["data"]["result"]["revenues"][3]['eps']) #EPS4
        eps_5=(js_eps["data"]["data"]["result"]["revenues"][4]['eps']) #EPS5
    except:                                                            #沒有任何eps資料就給所有變數0
        eps_time_1='0'
        eps_time_2='0'
        eps_time_3='0'
        eps_time_4='0'
        eps_time_5='0'
        eps_1='0'
        eps_2='0'
        eps_3='0'
        eps_4='0'
        eps_5='0'
    #-----營收成長率-----
    try:
        rev_time_1=(js_rev['data']['data']['result']['revenues'][0]['date']).replace("+08:00", "")[:4] #時間1
        rev_time_2=(js_rev['data']['data']['result']['revenues'][1]['date']).replace("+08:00", "")[:4] #時間2
        rev_time_3=(js_rev['data']['data']['result']['revenues'][2]['date']).replace("+08:00", "")[:4] #時間3
        rev_time_4=(js_rev['data']['data']['result']['revenues'][3]['date']).replace("+08:00", "")[:4] #時間4
        rev_time_5=(js_rev['data']['data']['result']['revenues'][4]['date']).replace("+08:00", "")[:4] #時間5
        rev_1=(js_rev['data']['data']['result']['revenues'][0]['revenueYoY'])+'%' #營收年增率1
        rev_2=(js_rev['data']['data']['result']['revenues'][1]['revenueYoY'])+'%' #營收年增率2
        rev_3=(js_rev['data']['data']['result']['revenues'][2]['revenueYoY'])+'%' #營收年增率3
        rev_4=(js_rev['data']['data']['result']['revenues'][3]['revenueYoY'])+'%' #營收年增率4
        rev_5=(js_rev['data']['data']['result']['revenues'][4]['revenueYoY'])+'%' #營收年增率5
    except:                                                                       #沒有任何營收年增率資料就給所有變數0
        rev_time_1='0'
        rev_time_2='0'
        rev_time_3='0'
        rev_time_4='0'
        rev_time_5='0'
        rev_1='0'
        rev_2='0'
        rev_3='0'
        rev_4='0'
        rev_5='0'
    #-----合理股價-----
    div_balance=(round((float(DIV[0])+float(DIV[1])+float(DIV[2])+float(DIV[3])+float(DIV[4]))/5)) #計算五年平均股利
    if div_balance==0:                                                                             #無任何股利發放
        price='無股利發放，謹慎評估'
    else:
        price=str(div_balance/0.04)
    stock = {'股票代碼':code, '股票名稱':name,
            '所屬年度1':div_time_1, '所屬年度2':div_time_2,
            '所屬年度3':div_time_3, '所屬年度4':div_time_4,
            '所屬年度5':div_time_5, '總股利1':DIV[0],
            '總股利2':DIV[1], '總股利3':DIV[2],
            '總股利4':DIV[3], '總股利5':DIV[4],
            '現金殖利率1':YIE[0], '現金殖利率2':YIE[1],
            '現金殖利率3':YIE[2], '現金殖利率4':YIE[3],
            '現金殖利率5':YIE[4], '時間1':eps_time_1,
            '時間2':eps_time_2, '時間3':eps_time_3,
            '時間4':eps_time_4, '時間5':eps_time_5,
            'EPS1':eps_1, 'EPS2':eps_2,
            'EPS3':eps_3, 'EPS4':eps_4,
            'EPS5':eps_5, '時間1':rev_time_1,
            '時間2':rev_time_2, '時間3':rev_time_3,
            '時間4':rev_time_4, '時間5':rev_time_5,
            '營收年增率1':rev_1, '營收年增率2':rev_2,
            '營收年增率3':rev_3, '營收年增率4':rev_4,
            '營收年增率5':rev_5, '合理股價':price}

    print('已存入')
    result = col.insert_one(stock)
    time.sleep(2)
for i in range(len(stock_range.stock_code)):
    print('讀取第'+str(i+1)+'檔')
    #代號名稱
    code=stock_range.stock_code[i]
    name=stock_range.stock_name[i]
    try:
        url='https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.dividends;action=combineCashAndStock;date=;limit=100;showUpcoming=true;sortBy=-date;symbol='+code+'.TW?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=3afqr1ti8kpa3&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true'
        res=requests.get(url)
        js=res.json()
        url_eps="https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.revenues;period=year;symbol="+code+".TW?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=0cjgjdpi8joq1&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true"
        res_eps=requests.get(url_eps)
        js_eps = res_eps.json()
        url_rev="https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.revenues;period=year;symbol="+code+".TW?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=0ag40mpi8jrlp&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true"
        res_rev=requests.get(url_rev)
        js_rev=res_rev.json()
        if 'data' in js_rev :
            print('第一種')
            search()
        elif 'data' not in js_rev :
            print('第二種')
            url='https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.dividends;action=combineCashAndStock;date=;limit=100;showUpcoming=true;sortBy=-date;symbol='+code+'.TWO?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=790g11pi8litg&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true'
            res=requests.get(url)
            js=res.json()
            url_eps='https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.revenues;period=year;symbol='+code+'.TWO?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=790g11pi8litg&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true'
            res_eps=requests.get(url_eps)
            js_eps = res_eps.json()
            url_rev='https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.revenues;period=year;symbol='+code+'.TWO?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=790g11pi8litg&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true'
            res_rev=requests.get(url_rev)
            js_rev=res_rev.json()
            search()

    except: 
        print('-----除外-----')
        print(code)
        print('-----除外-----')
