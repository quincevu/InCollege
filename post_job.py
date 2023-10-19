import mysql.connector
from Jobs_InputAPI import Jobs_API

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="welcome1",
    database="InCollege"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS Job1("
#                  "JobID binary(16) NOT NULL DEFAULT (UUID_TO_BIN(UUID(), TRUE)),"
#                  "username VARCHAR (50) NULL,"
#                  "Title VARCHAR (50) NULL,"
#                  "Employer VARCHAR (100) NULL,"
#                  "Salary Integer NULL,"
#                  "Location VARCHAR (200) NULL,"
#                  "Description VARCHAR (500) NULL,"
#                  "PRIMARY KEY (JobID))")
#                 # "FOREIGN KEY (username) REFERENCES userInfo(username))"





mycursor.execute("CREATE DATABASE IF NOT EXISTS InCollege")
mycursor.execute("USE InCollege")
mycursor.execute("SELECT username FROM userinfo WHERE inSession = 1")
userinfo = mycursor.fetchall()
if len(userinfo) != 0:
    userName = userinfo[0][0]

mydb.commit()

def del_or_post():
    print("1. Post a Job ")
    print("2. Delete a Job")
    print("3. Create a job using Job API")
    option = input()
    option_list = ["1", "2", "3"]
    while option not in option_list:
        option = input("Invalid option, please choose again")
    if option == "1":
        post_job()
        return "home"
    if option == "2":
        delete_job()
        return "home"
    if option == "3":
        Jobs_API()
        return "home"


#Let the user to post a job and save it on replit databse
def post_job():
    mycursor.execute("SELECT COUNT(*) from Job1")
    result = mycursor.fetchone()
    print(result)
    if result[0] >=10:
        print("Job capacity is full")

    else:  # redundant condition check
        print("Enter job:")
        title_in = input("Title:")
        posterName_in = input("Poster Name:")
        description_in = input("Description:")
        employer_in = input("Employer:")
        location_in = input("Location: ")
        salary_in = input("salary:")

        
        mycursor.execute(
            "INSERT INTO Job1 (Title, PosterName, Employer, Salary, Location, Description, userName)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (title_in , posterName_in, employer_in, salary_in, location_in, description_in, userName))
        new_job_notification(title_in)
        mydb.commit()
    return "home"


def delete_job():
    sql = "SELECT JobID, Title, Employer, Salary, Location, Description, username  FROM Job1 WHERE userName = %s"
    user = (userName,)
    mycursor.execute(sql,user)
    myresult = mycursor.fetchall()

    #printing available jobs
    for x in myresult:
        print(x)

    print("Enter the ID of the job you want to delete:")
    input_id = input()

    query = "SELECT username,appliedJobs,Title  FROM JobsApplied WHERE  appliedJobs = %s"
    id = (input_id,)
    mycursor.execute(query, id)
    notif = mycursor.fetchall()
    for i in range(len(notif)):
        if input_id == notif[i][1]:
            mycursor.execute(f"INSERT INTO JobsApplied (Username, deletedJobs,Title,appliedJobs)"
                             f"VALUES ('{notif[i][0]}', '{1}', '{myresult[i][1]}','{notif[i][1]}')")
            mydb.commit()

    #deleting job from the table
    sql2 ="DELETE FROM Job1 WHERE JobID = %s "
    job_id = (input_id,)
    mycursor.execute(sql2, job_id)
    mydb.commit()

    # getting list of jobs user applied to
    #query = "SELECT username,appliedJobs FROM JobsApplied WHERE appliedJobs = %s"
    #applied= (input_id,)
    #mycursor.execute(query, applied)
    myresult2 = mycursor.fetchall()

    print("under construct")
    return "home"

# def jobs_added_textfile(title, description, poster_name, employer_name,location,salary):
#     #checks that there are not more than 10 jobs
#     if not check_num_of_jobs():
#         print(
#             "Your job cannot be posted at this time. Please check back later."
#         )
#         return "welcome"
#     return 

    #all news job from the file go into the database
    # mycursor.execute(
    #     "INSERT INTO Job1 (Title, Poster Name, Employer, Salary, Location, Description)"
    #     "VALUES (%s, %s, %s, %s, %s, %s)",
    #     (title, description, poster_name, employer_name, location, salary))
    # mydb.commit()
    

#check number of jobs 
def check_num_of_jobs():
    numJobs = mycursor.execute("SELECT Title FROM Job1") 
    result = mycursor.fetchall()
    numJobs=len(result)
    #print(numAccounts)
    if (numJobs >= 10):
        return False
    return True



def new_job_notification(job_title):
    mycursor.execute("SELECT username FROM userInfo")
    result = mycursor.fetchall()
    notification = "A new job " + job_title + " has been posted"
    for i in range(len(result)):
        # print(user)  # debugging
        user_notification_table = result[i][0] + "_notification"

        mycursor.execute(f"INSERT INTO {user_notification_table} (notification, read_status) VALUES "
                       f"('{notification}','0')")

        # mycursor.execute(f"INSERT INTO {user_notification_table}  VALUES ({notification}, false")
        # query = "INSERT INTO " + user_notification_table + " (notification, read_status) VALUES (%s, FALSE)"
        # mycursor.execute(query, notification)

        mydb.commit()
