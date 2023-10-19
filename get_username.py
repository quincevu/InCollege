import mysql.connector

passwordCorrect = False
userNameCorrect = False
loginSuccess = False
maxUser = False

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="welcome1",
    database="InCollege"
)


def get_username():
    cursor = mydb.cursor()
    cursor.execute("SELECT username FROM UserInfo WHERE inSession = 1")
    userInfo = cursor.fetchall()
    cursor.close()
    # cursor.close()
    if len(userInfo) != 0:
        userName = userInfo[0][0]
        return userName
