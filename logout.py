import mysql
from welcome import welcome

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="welcome1",
    database="InCollege"
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS InCollege")
# cursor.execute("USE InCollege")


def logout():
    cursor.execute("SELECT username FROM UserInfo WHERE inSession = 1")
    userInfo = cursor.fetchall()
    userName = userInfo[0][0]

    cursor.execute("UPDATE UserInfo SET inSession = %s WHERE username = %s", (0, userName))
    mydb.commit()

    mydb.close()


