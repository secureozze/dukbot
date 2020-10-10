from crawl import get_schedule
import db_functions as db
import button_maker

def controller(bot):
    '''
      sutja = random.randint(1, 10)
    if(sutja%2==0):
        rand_result = 1
    else:
        rand_result = 0
    '''

    if bot.state == "/start":
        bot.send_img()
        bot.send_message_with_keyboard("여어! 히사시부리~! 덕질은 처음인건가..\n아래 버튼으로 그룹을 골라봐",button_maker.inline_sample())


    elif bot.state == "again" or bot.data == "/start":
        bot.send_img()
        bot.send_message_with_keyboard("야래야래,, 또 왔군,, 훗\n아래 버튼으로 그룹을 골라봐",button_maker.inline_sample())

    elif bot.state == "month":
        group = db.get_group(bot.chat_id)
        if not bot.data.isdigit():
            if "월" in bot.data:
                result = db.get_schedule(group,int(bot.data[:-1]))
                bot.send_message(result)
                bot.send_message("{}쨔응의 스케줄은 잘 확인했겠지? 훗\n다음에 또 필요하면 /start를 입력해라. 아디오스".format(group))
                bot.send_img()
                db.insert_state(bot.chat_id, "again")
            else:
                bot.send_message("몇 월인지 다시 입력하라굿!")

        else:
            result = db.get_schedule(group,int(bot.data))
            bot.send_message(result)
            bot.send_message("{}쨔응의 스케줄은 잘 확인했겠지? 훗\n다음에 또 필요하면 /start를 입력해라. 아디오스".format(group))
            '''
                else:
                bot.send_message("{}쨔응의 스케줄은 잘 확인했겠지? 훗\n특별히 이번에는 {}쨔응의 검색어 트랜드도 알려주지\n내가 필요하면 /start를 입력해라".format(group,group))
                bot.send.img2(group)
            '''
            db.insert_state(bot.chat_id,"again")