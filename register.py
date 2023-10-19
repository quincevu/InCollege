"""username and password should also get hashed in the DB for searching convenience
why, because it looks like we are not going to use SQL in this project. Not that we shouldn't, but everyone should have fundamental knowledge of SQL, which umm, idk if yall wanna do that.
so, we can keep storing data in text files and optimize the searching functions for such purposes.
for example, we can concatenate "u-" to the front of all usernames and "p-" to the front of all passwords. Then for all searching queries we concat the input once more to search for things in the db
however, I must say that I personally think that we should adapt SQL in some forms because the further we get into development, the more inconvenient text file storing style will be. #quang
"""

import mysql.connector
from valid_major_list import valid_major_list


# connecting database
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="welcome1",
    database="InCollege"
)

cursor = mydb.cursor(buffered=True)

# cursor.execute("CREATE DATABASE IF NOT EXISTS InCollege")
# cursor.execute("USE InCollege")


# cursor = mydb.cursor()


valid_majors = valid_major_list()
valid_languages = ["English", "Spanish"]


def register():
    # CHECK IF THERE ARE ALREADY 10 ACCOUNTS
    if not number_of_account_check():
        print(
            "We ran out of slots for new members. Please log in or come back later!"
        )
        return "welcome"
    print(
        "Welcome to InCollege. Please choose your username. A valid username must be fewer than 32 characters and must not be empty: "
    )
    # username and password register & validation
    new_username = input()
    while not new_username_check(new_username):
        new_username = input()
    new_password = input(
        "Please choose a password. A valid password must be between 8 and 32 characters, containing at least 1 number, 1 uppercase character, and 1 special character: "
    )
    while not new_password_check(new_password):
        new_password = input()

    # first and last name typed in
    new_first_name = input("Type in your first name: ")
    new_last_name = input("Type in your last name: ")

    # title
    title = input("Please enter your title: ")

    # university
    university = input("Type in your university: ")

    # Account type either Standard or Plus
    print("Would you like to join our Plus accounts for $10/month? ")
    print("1- Yes, I would like to join the 10 dollar subscription. ")
    print("2- No, I am good with my standard account")
    option = input()
    option_list = ["1", "2"]
    while option not in option_list:
        option = input("Invalid option, please choose again!")
    if option == "1":
        account_type = "Plus"
    if option == "2":
        account_type = "Standard"

    # major
    major = input("Type in your major: ")
    while major not in valid_majors:
        major = input("Invalid major. Please try again: ")

    # preferred langauge
    lang = input("Choose your language preference (English or Spanish): ")
    while lang not in valid_languages:
        lang = input("Invalid choice. Please choose again (Type English or Spanish): ")

    # database input

    cursor.execute("INSERT INTO userInfo (username, Password, FirstName, LastName, University, Major, Title, Language,account_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (new_username, new_password, new_first_name, new_last_name,  university, major, title, lang,account_type))


    new_member_notification(new_first_name, new_last_name, new_username)

    message_and_notification_initialization(new_username)

    mydb.commit()
    print(
        "Registration successful! You will be required to log in using your new username and password."
    )
    return "login"

def register_from_textfile(username,first_name,last_name,password):
    # CHECK IF THERE ARE ALREADY 10 ACCOUNTS
    if not number_of_account_check():
        print(
            "We ran out of slots for new members. Please log in or come back later!"
        )
        return "welcome"
    # username and password register & validation
    new_username = username
    if (new_username_check(new_username)== False):
        print ("invalid username")
        return False
    new_password = password
        #"Please choose a password. A valid password must be between 8 and 32 characters, containing at least 1 number, 1 uppercase character, and 1 special character: "
    if(new_password_check(new_password)==False):
       print ("invalid password")
       return False

    # first and last name typed in
    new_first_name = first_name
    new_last_name = last_name

    # database input

    cursor.execute("INSERT INTO userInfo (username, Password, FirstName, LastName) VALUES (%s, %s, %s, %s)",
                   (new_username, new_password, first_name, last_name))


    new_member_notification(new_first_name, new_last_name, new_username)

    message_and_notification_initialization(new_username)

    mydb.commit()
    print(
        "Registration successful! You will be required to log in using your new username and password."
    )
    return "login"


def new_password_check(new_password):
    upper_check = False
    special_check = False
    number_check = False
    special_list = "!@#$%^&*?+_(){}|\`~<>"
    plen = len(new_password)
    if plen > 32:
        print("Password too long. Please try again!")
        return False
    elif plen < 8:
        print("Password too short. Please try again!")
        return False
    for i in new_password:
        if i.isupper():
            upper_check = True
        if i in special_list:
            special_check = True
        if i.isnumeric():
            number_check = True
    if not upper_check:
        print("Password must have at least one uppercase character.")
        return False
    if not number_check:
        print("Password must have at least one number.")
        return False
    if not special_check:
        print("Password must have at least one special character.")
        return False
    return True


def new_username_check(new_username):
    if len(new_username) > 32:
        print("Username too long!")
        return False
    if new_username.isspace():
        print("Username must not be empty!")
        return False
    if not check_username_existence(new_username):
        print(
            "Username already existed, please log in or choose another username!"
        )
        return False
    return True


def check_username_existence(Username):
    cursor.execute("SELECT username FROM userInfo")
    result_table = cursor.fetchall()
    # print(result_table.fetchall())
    if Username in result_table:
        return False
    return True


def number_of_account_check():
   # numAccounts=0
    numAccounts = cursor.execute("SELECT username FROM userInfo") 
    result=cursor.fetchall()
    numAccounts=len(result)
    #print(numAccounts)
    if (numAccounts >= 10):
        return False
    return True

def college_profile(filename):
   # numAccounts=0
    numAccounts = cursor.execute("SELECT Major,Title,University,Description,Education from userinfo")
    result=cursor.fetchall()
    #cursor.close()
    numAccounts=len(result)
    file1 = open(filename,"w")
    for row in result:
        file1.writelines(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+"\n"+"===="+"\n")
    file1.close
    
    return ()

def college_users(filename):
   # numAccounts=0
    numAccounts = cursor.execute("SELECT username,account_type from userinfo")
    result=cursor.fetchall()
    cursor.close()
    numAccounts=len(result)
    file1 = open(filename,"w")
    for row in result:
        file1.writelines(str(row[0])+","+str(row[1])+"\n")
    file1.close
    
    return ()

    




def new_member_notification(first_name, last_name, username):
    # send out notification to students about this new member
    cursor.execute("SELECT username FROM userInfo")
    result = cursor.fetchall()
    temp = first_name + " " + last_name + " has joined InCollege"
    notification = (temp,)
    for user in result:
        # print(user)  # debugging
        if user[0] != username:
            user_notification_table = user[0] + "_notification"
            query = "INSERT INTO " + user_notification_table + " (notification, read_status) VALUES (%s, FALSE)"
            cursor.execute(query, notification)
            mydb.commit()
    return

def message_and_notification_initialization(new_username):
    new_message_table = new_username + "_message"
    tuple1 = (new_message_table,)
    new_notification_table = new_username + "_notification"
    tuple2 = (new_notification_table,)
    cursor.execute("CREATE TABLE IF NOT EXISTS " + new_message_table +
                   " (sender VARCHAR(32) NOT NULL, message TEXT, read_status BOOLEAN)", )
    # still not very practical because this makes it look like sending letters
    cursor.execute("CREATE TABLE IF NOT EXISTS " + new_notification_table + " (notification TEXT, read_status BOOLEAN)")
    mydb.commit()
    return