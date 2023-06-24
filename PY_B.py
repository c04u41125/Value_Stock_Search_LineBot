import requests
import time

def now_price(code):
    url='https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.stockList;autoRefresh=1686883228169;fields=avgPrice%2Corderbook;symbols='+code+'.TW?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=1dfn9ndi8niqu&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true'
    res=requests.get(url)
    js=res.json()
    if js['data'] != []:
        if time.localtime().tm_hour > 13 and time.localtime().tm_wday:
            price=('今日收盤價:'+js['data'][0]['price'])
            return price
        elif time.localtime().tm_hour > 8 :
            price=('即時股價:'+js['data'][0]['price'])
            return price
        else:
            price=('最近收盤價:'+js['data'][0]['regularMarketPreviousClose'])
            return price
        # print(price)
    else:
        url='https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.stockList;autoRefresh=1686883228169;fields=avgPrice%2Corderbook;symbols='+code+'.TWO?bkt=&device=desktop&ecma=modern&feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=1dfn9ndi8niqu&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1891&returnMeta=true'
        res=requests.get(url)
        js=res.json()
        if time.localtime().tm_hour > 13 :
            price=('今日收盤價:'+js['data'][0]['price'])
            return price
        elif time.localtime().tm_hour > 8 :
            price=('即時股價:'+js['data'][0]['price'])
            return price
        else:
            price=('昨日收盤價:'+js['data'][0]['regularMarketPreviousClose'])
            return price
        # print(price)
# now_price('2330')