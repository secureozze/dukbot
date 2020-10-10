import requests
from config import config
config = config()
import db_functions as db

class telegrambot:

    def __init__(self):
        self.chat_id = None
        self.data = None
        self.name = None
        self.data_type = None
        self.message_id = None
        self.state = None

    def __call__(self, input_data):
        # 단순한 텍스트 입력일때
        if not 'callback_query' in input_data.keys():
            chat_id = input_data['message']['chat']['id']
            msg = input_data['message']['text']
            user_name = input_data['message']['chat']['last_name'] + input_data['message']['chat']['first_name']
            message_id = input_data['message']['message_id']

            self.chat_id = str(chat_id)
            self.data =msg
            self.name = user_name
            self.message_id = message_id
            self.data_type = "text"

        # inline keyboard 입력일때
        else:
            chat_id = input_data['callback_query']['from']['id']
            user_name = input_data['callback_query']['from']['first_name'] + input_data['callback_query']['from']['last_name']
            self.chat_id = str(chat_id)
            self.data = input_data['callback_query']
            self.name = user_name

            self.data_type = "inline_keyboard"


        # db 처리(사용자등록)
        is_new =db.is_new_member(self.chat_id)

        if is_new:
            db.insert_user(self.chat_id,self.name,state="/start")

        self.state = db.get_userinfo(self.chat_id)[2]

    def send_message(self,text):
        params = {'chat_id': self.chat_id, 'text': text}
        requests.post(config.SEND_MESSAGE, json=params)

    def send_message_with_keyboard(self,text,keyboard):
        params = {'chat_id': self.chat_id, 'text': text, 'reply_markup':keyboard}
        requests.post(config.SEND_MESSAGE, json=params)

    def send_photo(self,url):
        params = {'chat_id': self.chat_id, 'photo': url}
        requests.post(config.SEND_PHOTO, json=params)

    def send_img(self):
        params = {'chat_id': self.chat_id}
        requests.post(config.SEND_PHOTO, data=params, files={'photo':open("./photos/hello.png","rb")})

'''
    def send_img2(self, group):
        params = {'chat_id': self.chat_id}
        requests.post(config.SEND_PHOTO, data=params, files={'photo': open("./photos/{}.png".format(group), "rb")})
'''
