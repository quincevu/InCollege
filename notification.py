import mysql.connector
from get_username import get_username
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="welcome1",
    database="InCollege"
)

cursor = mydb.cursor()
cursor.execute("SELECT username FROM UserInfo WHERE inSession = 1")
userInfo = cursor.fetchall()
if len(userInfo) != 0:
     userName = userInfo[0][0]


def show_new_notification():
    current_user_notification_box = userName + "_notification"
    query = "SELECT notification FROM " + current_user_notification_box + " WHERE read_status = FALSE"
    cursor.execute(query)
    result = cursor.fetchall()
    for unit in result:
        print(unit[0])
    cursor.execute("UPDATE " + current_user_notification_box + " SET read_status = TRUE WHERE read_status = FALSE")
    mydb.commit()


