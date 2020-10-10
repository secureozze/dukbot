from flask import Flask,request
import requests
from bot import telegrambot
from text_controller import controller as tc
from inline_controller import controller as ic
import inline_controller



API_KEY = '1047646057:AAGojfwQ5slRQqKUfH-d1iZTuWSjOZ0EQo0'
SEND_MESSAGE = 'https://api.telegram.org/bot{token}/sendMessage'.format(token=API_KEY)
# 서버에서 telegram으로 사진을 보내주는 메소드
SEND_PHOTO = 'https://api.telegram.org/bot{token}/sendPhoto'.format(token=API_KEY)

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():

    if request.method == "POST":
        data = request.get_json()
        #init
        bot = telegrambot()

        #call
        bot(data)

        if bot.data_type == "text":
            tc(bot)
        elif bot.data_type == "inline_keyboard":
            ic(bot)




    return ''

if __name__ == "__main__":
    app.run(debug=True, host = "localhost",port = 5000)