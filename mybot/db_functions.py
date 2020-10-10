import pymysql

host_name = "localhost"
username = "root"
password = "toor!@"
database_name = "chatbot"

def make_connection():

    conn = pymysql.connect(
        host=host_name,  # DATABASE_HOST
        port=3306,
        user=username,  # DATABASE_USERNAME
        passwd=password,  # DATABASE_PASSWORD
        db=database_name,  # DATABASE_NAME
        charset='utf8'
    )
    return conn

def is_new_member(chat_id):

    conn = make_connection()
    curs = conn.cursor()

    sql = "SELECT count(*) FROM user WHERE chat_id={}".format(chat_id)

    curs.execute(sql)

    isExist = curs.fetchone()[0]

    conn.close()

    if isExist:
        return False
    else:
        return True

def get_userinfo(chat_id):

    conn = make_connection()
    curs = conn.cursor()
    sql = "SELECT * FROM user WHERE chat_id={}".format(chat_id)
    curs.execute(sql)

    result = curs.fetchone()

    conn.close()
    return result

def insert_user(chat_id,name,state=None):
    conn = make_connection()
    if not state:
        sql = "INSERT INTO user (chat_id,name) VALUE (%s,%s)"
        val = (chat_id, name)
    else:
        sql = "INSERT INTO user (chat_id,name,user_state) VALUE (%s,%s,%s)"
        val = (chat_id, name,state)

    mycursor = conn.cursor()
    mycursor.execute(sql,val)
    conn.commit()

    conn.close()

def insert_state(chat_id,state):

    conn = make_connection()
    curs = conn.cursor()
    sql = "UPDATE user SET user_state = %s WHERE chat_id=%s"
    val = (state,chat_id)
    curs.execute(sql,val)
    conn.commit()

    conn.close()


def insert_group(chat_id,group):

    conn = make_connection()
    curs = conn.cursor()
    sql = "UPDATE user SET selected_group = %s WHERE chat_id=%s"
    val = (group,chat_id)
    curs.execute(sql,val)
    conn.commit()

    conn.close()

def insert_schedule(group,text,i):

    conn = make_connection()
    curs = conn.cursor()
    sql = "INSERT INTO schedule (group,%s) VALUES (%s, %s) "
    val = (i,group,text)
    curs.execute(sql,val)
    conn.commit()

    conn.close()

def get_schedule(group,month):

    conn = make_connection()
    curs = conn.cursor()
    sql = "SELECT * FROM schedule WHERE id=(%s)"

    val = (group)
    curs.execute(sql,val)

    result = curs.fetchone()[month]

    conn.close()
    return result


def get_group(chat_id):

    conn = make_connection()
    curs = conn.cursor()
    sql = "SELECT selected_group FROM user WHERE chat_id=(%s)"

    val = (chat_id)
    curs.execute(sql,val)

    result = curs.fetchone()[0]

    conn.close()
    return result





if __name__ == "__main__":
    print(get_group("1015977813"))