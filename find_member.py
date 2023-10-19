import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="welcome1",
    database="InCollege"
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS InCollege")
cursor.execute("USE InCollege")


def find_member():

    user_first = input("Enter the person's first name: ")
    user_last = input ("Enter the person's last name")

    cursor.execute("SELECT FirstName, LastName FROM userInfo")
    result_table = cursor.fetchall()

    for i in range(0, len(result_table)):
        if result_table[i][0] == user_first and result_table[i][1] == user_last:
            print("This person is an InCollege member")
        else:
            print("This person is not an InCollege member")
        return "welcome"

    # user_list = open("userInfo.txt", "r")
    # for line in user_list:
    #     count = 0
    #     target_name = ""
    #     for word in line.split():
    #         count += 1
    #         if count == 3:
    #             target_name = target_name + word + " "
    #         if count == 4:
    #             target_name = target_name + word
    #     if target_name == user_first_last:
    #         print("They are in the system")
    #         return "welcome"
    # print("They are not in the system yet!")
    # return "welcome"
    