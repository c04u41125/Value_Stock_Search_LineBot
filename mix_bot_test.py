from flask import Flask, request
#https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.models import FlexSendMessage, TextSendMessage
from stock_range import stock_code,stock_dic,stock_name
from PY_B import now_price
from PY_C import DB_GET
from PY_D import SAVE_info
from PY_E import LOAD_info
import threading
token="6oduXIt+NO+ZScLq7S2t29+ddipFY2Oy6s02CTQDMd4NObKIYvMFu0QeclXhOtGpkcx4vStaFHl4R9gypjg5X8N8++4uTuWumQjEe3pXqzsONsZ5z545H8xykdbO0EL2AKBW53SCh6zri7rWH1XljAdB04t89/1O/w1cDnyilFU="

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot = LineBotApi(token)
true=True
key_world=['其他類別','金融業類別','服務業類別','科技類別','工業類別','上市櫃股票清單','水泥工業','食品工業','塑膠工業','紡織纖維','電機機械','電器電纜','化學工業','生技醫療','玻璃陶瓷','造紙工業',
                        '鋼鐵工業','橡膠工業','汽車工業','半導體業','電腦周邊','光電業','通信網路','電子組件','電子通路','資訊服務',
                        '其他電子','建材營造','航運業','觀光事業','保險業','貿易百貨','油電燃氣','其他類','文化創意','農業科技','電子商務'
                        ,'金控業','銀行業','證券業','使用說明']
previous_data = {}  #用以儲存上次data
@app.route("/", methods=['POST'])
def verify():
    global previous_data
    data = request.get_json()
    if data['events'][0]['message']['type']=='text' :   #判斷使用者輸入的是文字
        input_text=data['events'][0]['message']['text']
        if input_text in stock_name and input_text not in key_world:    #判斷使用者輸入的文字是關鍵字之外且在個股名稱清單中
            code=stock_dic[input_text]
            i=DB_GET(code)
            p=now_price(code)
            ans = f"{i}\n\n{p}"
            line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text=ans))
            previous_data=data                                          #儲存data
        elif input_text in stock_code and input_text not in key_world:  #判斷使用者輸入的文字是關鍵字之外且在個股代號清單中
            code=input_text
            i=DB_GET(code)
            p=now_price(code)
            ans = f"{i}\n\n{p}"
            line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text=ans))
            previous_data=data                                          #儲存data
        elif '存檔' in input_text :                         #如果使用者輸入存檔
            try:
                checkid=previous_data['events'][0]['source']['userId']
                userid=data['events'][0]['source']['userId']            #使用者LINE ID為table
                if checkid == userid :
                    userid=data['events'][0]['source']['userId']            #使用者LINE ID為table
                    code=previous_data['events'][0]['message']['text']      #上次查詢的個股代號為欄位
                    if code in stock_name and code not in key_world:
                        code=stock_dic[code]
                        i=DB_GET(code)
                        p=now_price(code)
                        ans = f"{i}\n\n{p}"
                        LI=threading.Thread(target=SAVE_info,args=(userid,code,ans,))
                        LI.start()
                        LI.join
                        line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text='已儲存'))
                    elif code in stock_code and code not in key_world:
                        i=DB_GET(code)
                        p=now_price(code)
                        ans = f"{i}\n\n{p}"
                        LI=threading.Thread(target=SAVE_info,args=(userid,code,ans,))
                        LI.start()
                        LI.join
                        line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text='已儲存'))
            except:
                line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text='請先查詢再存檔'))
        elif '讀取' in input_text:                          #如果使用者輸入讀取
            try:
                userid=data['events'][0]['source']['userId']            #使用者LINE ID為table
                LI=threading.Thread(target=LOAD_info,args=(userid,))
                LI.start()
                LI.join
                ans=LOAD_info(userid)
                line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text=ans))
            except:
                line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text='請先存檔後再讀檔'))
        elif input_text not in key_world:
            line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text='輸入股票不在範圍內'))

    return 'OK',200

if __name__ == "__main__":
    app.run(port=1012)