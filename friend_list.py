import mysql.connector
from Student_Profile import show_friend_profile
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


def show_friends():

    userName = get_username()

    query = "SELECT Username2 FROM Friend WHERE Username = %s"
    tuple1 = (userName, )
    cursor.execute(query, tuple1)
    result_table = cursor.fetchall()

    if len(result_table) == 0:
        print("No friends")
        return "home"
    for i in range(0, len(result_table)):
        command3 = "SELECT username, FirstName, LastName from userInfo WHERE username = %s"
        arg3 = (result_table[i][0], )
        cursor.execute(command3, arg3)
        friend = cursor.fetchall()
        print(friend)

    print("Select from the below")
    print("1. Remove a friend")
    print("2. Show friend's profile")
    print("3. Send message to a friend")
    print("0. Return ")
    selection = input()
    valid_inputs = ["0", "1", "2", "3"]


    while selection not in valid_inputs:
        selection = input("Please enter a valid input")

    if selection == "0":
        return "home"
    if selection == "1":
        return "remove_friend"
    if selection == "2":
        profileName = input("Enter the username of the profile you would like to see ")
        show_friend_profile(profileName)  # HAZARDOUS APPROACH. NEED TO BE FIXED ASAP
    if selection == "3":
        return send_message()


def display_friends():
    userName = get_username()
    query2 = "SELECT Username2 FROM friend WHERE  Username = %s"
    id2 = (userName,)
    cursor.execute(query2, id2)
    notif2 = cursor.fetchall()
    print("Display list of friend:")
    friend_list = []
    for i in range(len(notif2)):
        friend_list.append(notif2[i][0])
        print(notif2[i][0])
    return friend_list  # bruh, i don't like this but i had to just do this


def display_all_users():

    query3 = "SELECT username FROM userinfo"
    cursor.execute(query3)
    notif3 = cursor.fetchall()
    print("Display list of all Users:")
    for i in range(len(notif3)):
        print(notif3[i][0])


def send_message():
    userName = get_username()
    query = "SELECT username,account_type FROM userinfo WHERE  username = %s"
    username_tuple = (userName,)
    cursor.execute(query, username_tuple)
    notif = cursor.fetchall()
    #  Checking for plus accounts
    if notif[0][1] == "Plus":
        print("Do you want to display all users or your friends? Type in \"All users\", \"Friends only\", or \"No\": ")
        answer = input()
        options = ["All users", "Friends only", "No"]
        while answer not in options:
            answer = input("Invalid option, please choose again: ")
        if answer == "All users":
            display_all_users()
        elif answer == "Friends only":
            display_friends()
        person_name = input("Enter the username of the person you would like to send a message: ")
        message = input("Write your message: ")
        cursor.execute(f"INSERT INTO message (Sender,Receiver,userMessage) VALUES "
                       f"('{userName}','{person_name}','{message}')")
        mydb.commit()
        return "show_friends"
    # Checking for Standard accounts
    elif notif[0][1] == "Standard":  # this logical check is redundant, because it is True all the time
        friend_list = display_friends()
        person_name = input("Enter the username of the person you would like to send a message:  ")
        while person_name not in friend_list:
            person_name = input("You are not friends with that person, try another user: ")
        message = input("Write your desire message: ")
        msg_read_status = False  # default
        cursor.execute(f"INSERT INTO message (Sender, Receiver, userMessage, read_status) VALUES "
                       f"('{userName}','{person_name}','{message},'{msg_read_status}')")
        mydb.commit()
        return "show_friends"


def remove_friends():
    userName = get_username()
    friend = input("Please enter the username of the friend you would like to remove: ")

    cursor.execute("DELETE FROM Friend WHERE Username = %s and Username2 = %s", (userName, friend))
    cursor.execute("DELETE FROM Friend WHERE Username = %s and Username2 = %s", (friend, userName))

    selection = input("To return to friend list enter 1, to return home enter 0: ")

    valid_inputs = ["0", "1"]

    while selection not in valid_inputs:
        selection = input("Please enter a valid input")

    if selection == "0":
        return "home"
    show_friends()



# def show_friends():
#     user = input("Confirm username:")
#     if user in friends:
#         for friend in friends[user]:
#             print(friend)
#         return "home"
#     print("No connections to show.")
#     return "home"
#
#
# def remove_friends():
#     user = input("Confirm username:")
#     remove_person = input("Who would you like to remove?")
#     friends[user].remove(remove_person)
#     return "home"
