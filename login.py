import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="welcome1",
    database="InCollege"
)

# cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS InCollege")
# cursor.execute("USE InCollege")


def login():  # i can add the return option later, it's trivial


    cursor = mydb.cursor()
    username = input("Please type in your username: ")
    password = input("Please type in your password: ")
    # university = input("Please enter your university:")

    while not check_credential(username, password):
        print("Incorrect username or password.")
        username = input("Please type in your username: ")
        password = input("Please type in your password: ")
    print("Log in successful!")

    # storing user as in session
    cursor.execute("UPDATE UserInfo SET inSession = %s WHERE username = %s", (1, username))
    mydb.commit()

    cursor.close()
    return "home"


def check_credential(username, password):
    cursor = mydb.cursor()
    # getting username and password from database
    cursor.execute("SELECT username, Password FROM userInfo")
    result_table = cursor.fetchall()
    # print (result_table)

    # iterating through table to find corressponding username and password
    for row in result_table:
        if username == row[0] and password == row[1]:
            return True
    return False
