
#replykeyboard


def keyboard_button(text):

    keyboard = {
        'text' : text
    }

    return keyboard

def ReplyKeyboardMarkup(keyboard):

    ReplyKeyboardMarkup = {
        'keyboard' : keyboard
    }

    return ReplyKeyboardMarkup


def keyboard_sample():

    keyboard = []
    row = []


    row.append(keyboard_button("버튼111"))
    row.append(keyboard_button("버튼222"))

    keyboard.append(row)

    return ReplyKeyboardMarkup(keyboard)


#inline keyboard
def InlineKeyboardButton(text=None,callback_data=None):

    InlineKeyboardButton ={
        'text' : text,
        "callback_data" : callback_data
    }

    return InlineKeyboardButton

def InlineKeyboardMarkup(keyboard=None):

    InlineKeyboardMarkup = {
        'inline_keyboard' : keyboard
    }

    return InlineKeyboardMarkup

def inline_sample():

    keyboard = []
    row=[]

    row.append(InlineKeyboardButton(text="TWICE",callback_data="TWICE"))
    row.append(InlineKeyboardButton(text="ITZY",callback_data="ITZY"))
    keyboard.append(row)

    row = []
    row.append(InlineKeyboardButton(text="내 최애가 없잖아!",callback_data="NO"))

    keyboard.append(row)

    return InlineKeyboardMarkup(keyboard)

def inline_sample2():

    keyboard = []
    row=[]

    row.append(InlineKeyboardButton(text="좋아",callback_data="YES"))
    row.append(InlineKeyboardButton(text="괜찮아",callback_data="NO"))

    keyboard.append(row)

    return InlineKeyboardMarkup(keyboard)


if __name__ == "__main__":
    print(inline_sample())
