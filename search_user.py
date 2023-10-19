import home
import mysql.connector
# import uuid

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

#getting current user
cursor.execute("SELECT username FROM UserInfo WHERE inSession = 1")

userInfo = cursor.fetchall()
if len(userInfo) != 0:
    userName = userInfo[0][0]

def search_user():

    print("Enter 1.to search by contact's last name,\n 2. university \n 3. major: , \n 4. Return")
    option = input()
    valid_options = ["1", "2", "3", "4"]
    while option not in valid_options:
        option = input("Please enter a valid input")

    if option == "1":
        last_name()
    if option == "2":
        university()
    if option == "3":
        major()
    return "home"

#searching by last name

def last_name():

    contact_last = input("Enter your contact's last name: ")
    # getting username, first name and last name based on last name search
    command = "SELECT username, FirstName, LastName FROM userInfo where LastName = %s"
    arg = (contact_last,)
    cursor.execute(command, arg)
    result_table = cursor.fetchall()

    if len(result_table) == 0:
        print ("No member found")
        search_user()
    # print results
    for row in result_table:
        if row[2] == contact_last:
            print(row[0] + " " + row[1] + " "+ row[2])

    person_name = input("Enter the username of the person you would like to connect with ")

    # inserting requestee and requester into account 1 and account 2
    for row in result_table:
        if row[0] == person_name:
            requesteeName = row[0]
            cursor.execute(f"INSERT INTO friendRequests (Account1, Account2) VALUES ('{userName}', '{requesteeName}')")
            mydb.commit()
            search_user()
    search_user()


def university():
    uni = input("Enter your the university's name: ")

    command = "SELECT username, FirstName, LastName, University FROM userInfo WHERE University = %s"
    arg = (uni,)
    cursor.execute(command, arg)
    result_table = cursor.fetchall()

    if len(result_table) == 0:
        print ("No member found")
        search_user()

    for row in result_table:
        if row[3] == uni:
            print (row[0] + " " + row[1] + " "+ row[2])

    person_name = input("Enter the username of the person you would like to connect with ")

    for row in result_table:
        if row[0] == person_name:
            requesteeName = row[0]
            cursor.execute(f"INSERT INTO friendRequests (Account1, Account2) VALUES ('{userName}','{requesteeName}')")
            mydb.commit()
            search_user()
    print("Invalid Entry")
    return search_user()

def major():

    major = input("Enter your major's name: ")

    command = "SELECT username, FirstName, LastName, Major FROM userInfo WHERE Major = %s"
    arg = (major,)
    cursor.execute(command, arg)
    result_table = cursor.fetchall()

    if len(result_table) == 0:
        print ("No member found")
        search_user()

    for row in result_table:
         if row[3] == major:
             print(row[0] + " " + row[1] + " " + row[2])

    person_name = input("Enter the username of the person you would like to connect with ")

    for row in result_table:
         if row[0] == person_name:
             print(row[0])
             requesteeName = row[0]
             cursor.execute(f"INSERT INTO friendRequests (Account1, Account2) VALUES ('{userName}', '{requesteeName}')")
             mydb.commit()
             search_user()
    search_user()
