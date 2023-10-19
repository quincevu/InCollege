import mysql.connector
from get_username import get_username

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

# getting current user
# cursor.execute("SELECT username FROM UserInfo WHERE inSession = 1")
# userInfo = cursor.fetchall()
# if len(userInfo) != 0:
#     userName = userInfo[0][0]
#     print(userName)


def accept_request():
    userName = get_username()
    newFriend = input("Please enter the username of the person you would like to accept")
    cursor.execute(f"INSERT INTO Friend (Username, Username2) VALUES ('{userName}','{newFriend}')")
    cursor.execute(f"INSERT INTO Friend (Username, Username2) VALUES ('{newFriend}','{userName}')")

    mydb.commit()

    command = "DELETE FROM friendRequests WHERE Account1 = %s and Account2 = %s"
    args = (userName, newFriend)
    cursor.execute(command, args)

    mydb.commit()
    mydb.close()

    friend_requests()


def delete_request():
    userName = get_username()
    notFriend = input("Please enter the username of the person you would like to accept ")
    cursor.execute("DELETE FROM friendRequests WHERE Account1 = %s and Account2 = %s", (notFriend, userName))
    friend_requests()


def friend_requests():
    userName = get_username()
    command = "SELECT Account2 from friendRequests WHERE Account1 = %s"
    arg = (userName, )
    cursor.execute(command, arg)
    result_table = cursor.fetchall()
    print(result_table)
    if len(result_table) == 0:
        print ("You have no friend requests")
        return "home"

    print("You have friend requests from: ")
    for i in range(0, len(result_table)):
        command = "Select username, FirstName, LastName from userInfo WHERE username = %s"
        arg = (result_table[i][0], )
        cursor.execute(command, arg)
        result = cursor.fetchall()
        print(result)

    print("Please select from the following options")
    print("1. Accept Request")
    print("2. Delete Request")
    print("3. Return")
    selection = input()

    valid_inputs = ["1", "2", "3"]
    while selection not in valid_inputs:
        selection = input("Please enter a valid input")

    if selection == "1":
        accept_request()
    if selection == "2":
        delete_request()

    return "home"



