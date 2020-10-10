from urllib.request import Request, urlopen
from config import config
config = config()
API_KEY = '1047646057:AAGojfwQ5slRQqKUfH-d1iZTuWSjOZ0EQo0'

WEBHOOK = 'https://531c909c.ap.ngrok.io'
BOT_UPDATE = 'https://api.telegram.org/bot{API_KEY}/getUpdates?offset=54234681'.format(API_KEY=API_KEY)

# telegram과 bot과의 webhook 연결 해주는 메소드
BOT_SET_WEBHOOK = 'https://api.telegram.org/bot{API_KEY}/setWebhook?url={WEBHOOK_URL}' \
    .format(API_KEY=API_KEY, WEBHOOK_URL=WEBHOOK)

# telegram과 bot의 webhook을 끊어주는 메소드
BOT_DELETE = 'https://api.telegram.org/bot{API_KEY}/deleteWebhook'.format(API_KEY=API_KEY)


def bot_update_call():
    """
    bot 의 업데이트 정보를 출력하는 함수
    """
    request = Request(config.BOT_UPDATE)
    print(config.BOT_UPDATE)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)


def bot_set_webhook_call():
    """
    bot 의 Webhook 을 세팅하는 함수
    """

    # 내가 만든 봇이랑 webhook이 5000번 포트랑 연결
    request = Request(BOT_SET_WEBHOOK)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)


def delete_webhook():
    """
    bot 의 Webhook 을 제거하는 함수
    """
    request = Request(BOT_DELETE)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)


if __name__ == '__main__':

    #bot_info_call()
    delete_webhook()
    #bot_update_call()
    bot_set_webhook_call()
    #get_webhook_info()