import mysql.connector
from get_username import get_username

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

cursor = mydb.cursor()
username = get_username()


def check_unread_messages():  # check if there is unread messages, used when a user just logged in
    query = "SELECT Sender, userMessage FROM message WHERE Receiver = %s AND read_status = FALSE"
    username_tuple = (username,)
    cursor.execute(query, username_tuple)
    result = cursor.fetchall()
    if len(result) == 0:
        return False
    return result


def show_unread_messages():
    result = check_unread_messages()
    if not result:
        print("No unread message!")
        return False
    print("Unread messages are listed below: ")
    print(result)  # im not sure if it should be printed out this way. someone please check.
    mark_unseen_messages_as_read()
    return True


def mark_unseen_messages_as_read():  # mark messages as read when opening them for the first time
    query = "UPDATE message SET read_status = TRUE WHERE Receiver = %s AND read_status = FALSE"
    username_tuple = (username,)
    cursor.execute(query, username_tuple)
    # below is for testing only
    return check_unread_messages()


def show_all_messages():
    query = "SELECT Sender, userMessage FROM message WHERE Receiver = %s"
    username_tuple = (username,)
    cursor.execute(query, username_tuple)
    result = cursor.fetchall()
    if len(result) == 0:
        print("You have no messages!")
        return False
    print("All your messages are displayed below:")
    print(result)
    return True  # for testing only

