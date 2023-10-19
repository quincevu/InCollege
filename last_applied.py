#import get_username from get_username
import datetime
import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="welcome1",
    database="InCollege"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT username FROM UserInfo WHERE inSession = 1")
userInfo = mycursor.fetchall()
if len(userInfo) != 0:
    userName = userInfo[0][0]


def latest_applied():
    query1 = "SELECT InDtTm FROM JobsApplied WHERE Username = %s ORDER BY InDtTm DESC limit 1"
    args1 = (userName,)
    mycursor.execute(query1, args1)
    saved = mycursor.fetchall()
    print(saved)
    return saved[0][0]


def last_applied():
    current_time_stamp = datetime.datetime.now()
    if len(userInfo) != 0:
      time = current_time_stamp-latest_applied()
      #print()
      if (current_time_stamp-latest_applied()) > datetime.timedelta(days=7):
        print("Please apply for a job soon")
    return