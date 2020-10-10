import db_functions as db

def controller(bot):
    print(bot.data)

    data = bot.data['data']

    if(data=="TWICE"):
        bot.send_photo("http://newsimg.hankookilbo.com/2019/09/22/201909220881025371_1.jpg")
        bot.send_message("몇 월의 스케줄을 보고 싶어?")
        db.insert_state(bot.chat_id, 'month')
        db.insert_group(bot.chat_id, data)
    elif(data=="ITZY"):
        bot.send_photo("https://t1.daumcdn.net/liveboard/sweets/c88cff5564114f7090709ca8f2c450c7.JPG")
        bot.send_message("몇 월의 스케줄을 보고 싶어?")
        db.insert_state(bot.chat_id, 'month')
        db.insert_group(bot.chat_id, data)
    else:
        bot.send_message("와칸다,,, 완전 스미마셍하다,,, 하지만 날 믿고 기다려주겠나?\n금방 업데이트하도록 하지\n다시 시작하려면 /start를 입력하게")
        db.insert_state(bot.chat_id, 'again')