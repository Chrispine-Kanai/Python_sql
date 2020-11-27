from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user))
    db.commit()
    # log_id = cursor.lastrowid()
    # print("Added log {}".format(log_id))


def get_logs():
    sql = ("SELECT * FROM logs ORDER BY id DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)

def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s ORDER BY id DESC")
    cursor.execute(sql , (id,))
    result = cursor.fetchone()

    for row in result:
        print(row)

def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s ")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log updated")


def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s ")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log Deleted")
# add_log("This is log one","Tom")
# add_log("This is log two","Dick")
# add_log("This is log 3","Harry")

delete_log(3)
get_logs()