import friend_list
import mysql.connector
import home
from get_username import get_username


passwordCorrect = False
userNameCorrect = False
loginSuccess = False
maxUser = False

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="welcome1",
    database="InCollege"
)

cursor = mydb.cursor()
username = get_username()

# cursor.execute("CREATE DATABASE IF NOT EXISTS InCollege")
# cursor.execute("USE InCollege")

# fetching profile information
cursor.execute("SELECT username,FirstName,LastName,Major,Title,University,Description,Education"
               " FROM UserInfo WHERE inSession = 1")


userInfo = cursor.fetchall()

if len(userInfo) != 0:
    username = userInfo[0][0]
    


def check_profile():  # check if there profile exists,  according to my understanding of the epics,
    # if all the columns required to make a profile are empty then the profile does not exist, the columns required to make  a profile are title,
    #major, university, education and paragraph with info. however even if a few of these columns are filled it still counts as having a prfoile, its just an incomplete one
    # which is why here i have checked to see if all the required columns are empty and if it is, the the profile does not exist and 
    # the user gets the notification to create one
    #however the only issue wiht this is every time we try to register a new account, we are required to put in our title, major, uni and major 
    #which makes it seem like we have a profile, we should not be asked to inputted these details in the registration 
    # we can perhaps change that later on 
    # FROM UserInfo WHERE Major is NULL AND Title is NULL AND University is NULL AND Education is NULL AND Description is NULL AND


    # cursor = mydb.cursor()
    # query = "SELECT username from userinfo where insession = 1"
    # username_tuple = (username,)
    # cursor.execute(query, username_tuple)
    # result = cursor.fetchall()
    # if len(result) == 0:
    #      return False
    # return result

    cursor.execute("select * from userinfo where insession=1 and Education is NULL")
    userInfo = cursor.fetchall()
    #no_of_rows=userInfo[0]
    if len(userInfo): #< 7:
      #print(userInfo)
      #print(len(no_of_rows))
      return True
    else:
      return False


def edit_title():
    title = input("Please enter updated title")
    cursor.execute("UPDATE UserInfo SET Title = %s WHERE username = %s", (title, username))
    mydb.commit()
    return edit_profile()


def edit_major():
    major = input("Please enter updated major")

    cursor.execute("UPDATE UserInfo SET Major = %s WHERE username = %s", (major, username))
    mydb.commit()
    return edit_profile()


def edit_university():
    university = input("Please enter updated university")

    cursor.execute("UPDATE UserInfo SET University = %s WHERE username = %s", (university, username))
    mydb.commit()
    return edit_profile()


def edit_about():
    about = input("Please enter updated about information")

    cursor.execute("UPDATE UserInfo SET Description = %s WHERE username = %s", (about, username))
    mydb.commit()
    return edit_profile()


def edit_education():

    education = input("Please enter updated education")
    command ="UPDATE UserInfo SET Education = %s WHERE username = %s"
    args = (education, username)
    cursor.execute(command, args)
    mydb.commit()
    return edit_profile()


def edit_experience():
    # "SELECT count(*) AS New_column_name FROM information_schema.columns where table_name = 'Persons';"
    # "SELECT COUNT(username) FROM userInfo"
    command = "SELECT COUNT(username) FROM Jobs WHERE username = %s "
    arg = (username, )
    cursor.execute(command, arg)
    result = cursor.fetchall()
    print(result)
    if result[0][0] > 3:
        print ("You cannot add any more jobs")
        return edit_profile()

    cursor.execute("SELECT * FROM Jobs WHERE username = %s", arg)
    result_table = cursor.fetchall()
    print(result_table)

    print("To add a new job to enter 1")
    print("To return enter 0")
    selection = input()

    valid_inputs = ["0", "1"]
    while selection not in valid_inputs:
        selection = input("Enter a valid input")

    if input == "0":
        return edit_profile()

    Title = input("Please enter the position title ")
    Employer = input("Please enter the employer ")
    startDate = input("Please enter the start date ")
    endDate = input("Please enter the end date or current if still working ")
    location = input("Please enter the job location ")
    Description = input("Please enter a description of the job ")

    cursor.execute(f"INSERT INTO Jobs (username, Title, Employer, StartDate, EndDate, Location, Description) "
                   f"VALUES ('{username}', '{Title}', '{Employer}','{startDate}', '{endDate}','{location}','{Description}')")
    mydb.commit()

    return edit_profile()




# allows user to select where they want to make edits to file



def show_profile():
    # cursor.execute("SELECT username,FirstName,LastName,Major,Title,University,Description,Education"
    #               " FROM UserInfo WHERE inSession = 1")
    #
    # userInfo = cursor.fetchall()
    arg = (username, )
    cursor.execute("SELECT Title, Employer, StartDate, EndDate, Location, Description FROM Jobs WHERE Username = %s ", arg)
    experience = cursor.fetchall()

    lastName = userInfo[0][2]
    firstName = userInfo[0][1]
    username = userInfo[0][0]
    title = userInfo[0][4]
    major = userInfo[0][3]
    university = userInfo[0][5]
    about = userInfo[0][6]
    education = userInfo[0][7]

    print(firstName,lastName)
    print(username)
    print(title)
    print("School: " + university)
    print("Major: " + major)
    print("About:")
    print(about)
    print("Education:")
    print(education)
    print("Experience: ")
    print(experience)

    option = input("Enter 1 to make changes to your profile or 0 to return")
    print (option)
    valid_inputs = ["0","1"]


    while option not in valid_inputs:
        print("here1")
        print("Invalid input!")
        option = input("Enter 1 to make changes to your profile or 0 to return")
    if option == "1":
        edit_profile()

    return "home"


def edit_profile():

    print("Please select the area to which you want to make changes")
    print("1. Title")
    print("2. Major")
    print("3. University")
    print("4. About")
    print("5. Experience")
    print("6. Education")
    print ("7. View your profile")
    print("0. Return")

    selection = input()
    valid_inputs = ["0", "1", "2", "3", "4", "5", "6", "7"]

    while selection not in valid_inputs:
        selection = input("Invalid option, please try again: ")

    if selection == "1":
        edit_title()
    if selection == "2":
        edit_major()
    if selection == "3":
        edit_university()
    if selection == "4":
        edit_about()
    if selection == "5":
        edit_experience()
    if selection == "6":
        edit_education()
    if selection == "7":
        show_profile()
    if selection == "0":
        return "home"

def show_friend_profile(name):

    command = "SELECT username,FirstName,LastName,Major,Title,University,Description,Education FROM UserInfo WHERE username = %s"
    arg = (name, )
    cursor.execute(command, arg)
    user = cursor.fetchall()

    arg = (name,)
    cursor.execute("SELECT Title, Employer, StartDate, EndDate, Location, Description FROM Jobs WHERE Username = %s ",
                  arg)
    experience = cursor.fetchall()

    lastName = user[0][2]
    firstName = user[0][1]
    #username = user[0][0]
    title = user[0][4]
    major = user[0][3]
    university = user[0][5]
    about = user[0][6]
    education = user[0][7]

    print(firstName, lastName)
    print(username)
    print(title)
    print("School: " + university)
    print("Major: " + major)
    print("About:")
    print(about)
    print("Education:")
    print(education)
    print("Experience: ")
    print(experience)


