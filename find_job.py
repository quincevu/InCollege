from valid_major_list import valid_major_list
import mysql.connector
# from home import home
import datetime
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="welcome1",
    database="InCollege"
)

mycursor = mydb.cursor()

# getting current user
mycursor.execute("SELECT username FROM UserInfo WHERE inSession = 1")
userInfo = mycursor.fetchall()
if len(userInfo) != 0:
    userName = userInfo[0][0]


def save_job(jobid):
    mycursor.execute(f"INSERT INTO JobsApplied (username,savedJobs)"
                     f"VALUES ('{userName}', '{jobid}')")
    mydb.commit()
    # print(jobid)

    # getting list of jobs user applied to

    query1 = "SELECT savedJobs,Username,Reason,InDtTm FROM JobsApplied WHERE Username = %s ORDER BY InDtTm DESC limit 1"

    # last_applied_job= "SELECT InDtTm from JobsApplied  "
    args1 = (userName,)
    mycursor.execute(query1, args1)
    saved = mycursor.fetchall()

    # creating list of job ids for the jobs user applied to
    appliedJ1 = []

    for x in range(len(saved)):
        appliedJ1.append(saved[x][0])

    for u in appliedJ1:
        query2 = "SELECT JobID, Title, Employer, Salary, Location, Description FROM Job1 WHERE JobID = %s"
        arg = (jobid,)
        mycursor.execute(query2, arg)
        job = mycursor.fetchall()
        print(job)

    print("Would you like to unmark one of the saved jobs?")
    print("1. Yes")
    print("2. Return")
    # getting input
    option = input()
    valid_options = ["1", "2"]
    while option not in valid_options:
        option = input("Please enter a valid option: ")

    # returning home if chosen
    if option == "1":
        print("Enter ID of the Job you want to unmark: ")
        input_id = input()
        sql2 = "DELETE FROM jobsapplied WHERE savedJobs = %s "
        job_id = (input_id,)
        mycursor.execute(sql2, job_id)
        mydb.commit()

        return find_job()
    if option == "2":
        return find_job()

def jobs_saved():
    mycursor.execute("SELECT username, savedJobs FROM JobsApplied")
    SavedJobs = mycursor.fetchall()

    file2 = open("MyCollege_savedJobs.txt", "w")

    for row in SavedJobs:
        file2.writelines(str(row[0])+","+str(row[1])+"\n"+"===="+"\n")
    file2.close

    return ()

def apply(jobid):
    # checking if user has already applied to job
    sql = "SELECT AppliedJobs FROM JobsApplied WHERE AppliedJobs = %s AND Username = %s"
    args = (jobid, userName)
    mycursor.execute(sql, args)
    result = mycursor.fetchall()
    if result:
        print("You already applied for this job")
        return find_job()

    gradDate = input("Enter your expected graduation date: ")
    startDate = input("Enter your desired start date: ")
    Reason = input("Why would you be a good fit for this position?")
    
    #writing reason for application to applied jobs api file
    f_in = open('MyCollege_appliedJobs.txt', 'r')
    

    #     insert into table
    mycursor.execute(f"INSERT INTO JobsApplied (Username, appliedJobs, gradDate, startDate, Reason)"
                     f"VALUES ('{userName}', '{jobid}', '{gradDate}', '{startDate}', '{Reason}')")
    mydb.commit()

    #sql = f"SELECT * FROM Job1 WHERE JobID = {jobid}" 
    # mycursor.execute(sql, args)
    # result = mycursor.fetchall()
    # call the write to file function

    return find_job()

    return find_job()

def jobs_applied():
    mycursor.execute("SELECT username, Reason FROM JobsApplied")
    AppliedJobs = mycursor.fetchall()

    file1 = open("MyCollege_appliedJobs.txt", "w")

    for row in AppliedJobs:
        file1.writelines(str(row[0])+","+str(row[1])+"\n"+"===="+"\n")
    file1.close

    return ()


def all_jobs():
    mycursor.execute("SELECT Title, Employer, Description, Location FROM Job1")
    JobFile = mycursor.fetchall()

    j_file = open("MyCollege_jobs.txt", "w")

    for row in JobFile:
        j_file.writelines(str(row[0])+","+str(row[1])+","+str(row[2])+"\n"+"===="+"\n")
    j_file.close

    # print("here")
    return ()


def find_job():
    show_number_of_applied_jobs()

    query = "SELECT appliedJobs, Title FROM JobsApplied WHERE username = %s AND deletedJobs = %s "
    arguments = (userName, 1,)

    mycursor.execute(query, arguments)
    notif = mycursor.fetchall()

    if len(notif) != 0:
        print("Unfortunately the following jobs you applied for have been deleted: ")
        for i in range(len(notif)):
            print(notif[i][0], notif[i][1])
    # printing menu for selection
    print("Which would you like to see")
    print("1. Available jobs")
    print("2. Jobs Applied for")
    print("3. Jobs not applied for")
    print("4. Return")

    # getting input
    option = input()
    valid_options = ["1", "2", "3", "4"]
    while option not in valid_options:
        option = input("Please enter a valid option")

    # returning home if chosen
    if option == "4":
        return "home"

    # getting list of jobs user applied to
    query = "SELECT appliedJobs FROM JobsApplied WHERE Username = %s"
    args = (userName,)
    mycursor.execute(query, args)
    applied = mycursor.fetchall()
    # creating list of job ids for the jobs user applied to
    appliedJ = []

    for x in range(len(applied)):
        appliedJ.append(applied[x][0])

    # printing list of applied jobs
    if option == "2":
        for id in appliedJ:
            query2 = "SELECT Title, Employer, Salary, Location, Description FROM Job1 WHERE JobID = %s"
            arg = (id,)
            mycursor.execute(query2, arg)
            job = mycursor.fetchall()
            print(job)
        return find_job()

    # getting list of all jobs
    mycursor.execute("SELECT JobID, Title, Employer, Salary, Location, Description, username  FROM Job1 ")
    myresult = mycursor.fetchall()

    # printing unapplied jobs
    if option == "3":
        for i in range(len(myresult)):
            jid = myresult[i][0]
            if str(jid) not in appliedJ:
                print(myresult[i][0], myresult[i][1], myresult[i][2])

    # printing all job titles and their employer and telling which has been applied to
    if option == "1":
        print("Available Jobs:")
        for i in range(len(myresult)):
            if str(myresult[i][0]) in appliedJ:
                print("Already applied", myresult[i][0], myresult[i][1], myresult[i][2])
                continue
            else:
                print(myresult[i][0], myresult[i][1], myresult[i][2])

    id = input("If you would like to see more information for a job please enter the associated Job ID ")

    # check if valid id
    for i in range(len(myresult)):
        if myresult[i][0] == int(id):
            print("Job Title: ", myresult[i][1])
            print("Employer: ", myresult[i][2])
            print("Salary: ", myresult[i][3])
            print("Location: ", myresult[i][4])
            print("Job Description: ", myresult[i][5])
            poster = myresult[i][6]
            break

    print("Would you like to apply for this job or save it for later?")
    print("1. Apply")
    print("2. Save it for later")
    print("3. Return")
    choice = input()
    valid_inputs = ["1", "2", "3"]

    while choice not in valid_inputs:
        choice = input("Please enter a valid input ")

    if choice == "2":
        return save_job(int(id))
    if choice == "3":
        return find_job()
    if choice == "1":
        if poster == userName:
            print("You cannot apply to jobs you posted")
            return find_job()
        return apply(int(id))

def show_number_of_applied_jobs():
    mycursor.execute("SELECT COUNT(*) FROM JobsApplied")
    result = mycursor.fetchall()
    print(f"You have applied for {result} jobs")  # if this causes an error, maybe change %s to %d
    return result

    # old code
    # def find_job():

    # type_of_job, major, visa_sponsor, relocation
    #
    # print("What type of job are you looking for?")
    # print("1. Avialable Jobs List")
    # print("2. Entry-level")
    # print("3. Internship")
    # print(
    #     "4. Full-Time"
    # )
    #
    # option = input()
    # option_list = ["1", "2", "3","4"]
    # while option not in option_list:
    #     option = input("Invalid option, please choose again")
    # if option == "1":
    #     available_jobs()
    #     return find_job()
    # if option == "2":
    #     type_of_job = "Entry-level"
    #
    # if option == "3":
    #     type_of_job = "Internship"
    #
    # if option == "4":
    #     type_of_job = "Full Time"

    # print("Which would you like to see")
    # print("1. Availabe jobs")
    # print("2. Jobs Applied for")
    # print("3. Jobs not applied for")
    # print("4. Return")
    #
    # option = input()
    # valid_options = ["1", "2", "3", "4"]
    # while option not in valid_options:
    #     option = input("Please enter a valid option")
    #
    # if option == 1:
    #     available_jobs()
    # if option == 2:
    #
    # if option == 3:
    #
    # if option == 4:
    #     return "home"

    # major = input("What is your major?")
    # check_valid_major_list = valid_major_list()
    # while major not in check_valid_major_list:
    #     major = input(
    #         "We could not verify your major, please try again, or choose a different major: "
    #     )
    # relocation = input(
    #     "Are you willing to relocation if required by the company? Please type in \"Yes\" or \"No\": "
    # )
    # relocation_option = ["Yes", "No"]
    # while relocation not in relocation_option:
    #     relocation = input(
    #         "Invalid choice, please type in \"Yes\" or \"No\": ")
    # #all info collected. time to send a query to the DB for info
    # print("Thank you, here are all relevant job posts we found: ")
    # print("No job postings were found that match your criteria.")
    #
    # print("Page still under construction.")
    # return "home"

    # def find_job():
    #     print("Which would you like to see")
    #     print("1. Availabe jobs")
    #     print("2. Jobs Applied for")
    #     print("3. Jobs not applied for")
    #     print("4. Return")
    #
    #     option = input()
    #     valid_options = ["1", "2", "3", "4"]
    #     while option not in valid_options:
    #         option = input("Please enter a valid option")
    #
    #     if option == 4:
    #         return "home"
    #
    #     query = "SELECT appliedJobs FROM JobsApplied WHERE Username = %s and appliedJobs != %s"
    #     args = (userName,None)
    #     mycursor.execute(query, args)
    #     applied = mycursor.fetchall()
    #
    #     appliedJ =[]
    #     for i in range(applied):
    #         appliedJ = appliedJ.append(applied[i][0])
    #
    #     if option == 1:
    #         available_jobs(appliedJ)
    #     if option == 2:
    #         appliedJobs(appliedJ)
    #     if option == 3:
    #         unappliedJobs(appliedJ)

    # mycursor.execute("SELECT JobID, Title, Employer, Salary, Location, Description, username  FROM Job1 ")
    # myresult = mycursor.fetchall()
    #
    # print("Availabe Jobs:")
    # for x in range(len(myresult)):
    #     print(myresult[x][0] + " " + myresult[x][1] + " " + myresult[x][2])
    #
    # id = input("If you would like to see more information for a job please enter the associated Job ID")
    #
    # check if valid id
    # for i in range(len(myresult)):
    #     if myresult[i][0] == id:
    #         print("Job Title: ", myresult[i][1])
    #         print ("Employer: ", myresult[i][2])
    #         print("Salary: ",myresult[i][3])
    #         print("Location: ", myresult[i][4])
    #         print("Job Description: ", myresult[i][5])
    #         poster = myresult[i][6]
    #         break
    #
    # print("Would you like to apply for this job?")
    # print("1. Yes")
    # print("2. Return")
    # choice = input()
    # valid_inputs = ["1", "2"]
    #
    # while choice not in valid_inputs:
    #     choice = input("Please enter a valid input ")
    #
    # if choice == 2:
    #     return available_jobs()
    # if choice == 1:
    #     if poster == userName:
    #         print("You cannot apply to jobs you posted")
    #         return available_jobs()
    #     return apply(id)

# def appliedJobs(applied):
#
#     # query = "SELECT appliedJobs FROM JobsApplied WHERE Username = %s"
#     # args = (userName, )
#     # mycursor.execute(query, args)
#     # applied = mycursor.fetchall()
#
#     for id in applied:
#         query2 = "SELECT Title, Employer, Salary, Location, Description FROM Job1 WHERE JobID = %s"
#         arg = (applied, )
#         mycursor.execute(query2, arg)
#         job = mycursor.fetchall()
#         print(job)
#
# def unappliedJobs(applied):
#
#     mycursor.execute("SELECT JobID, Title, Employer, Salary, Location, Description, username  FROM Job1 ")
#     myresult = mycursor.fetchall()
#
#     for i in range (myresult):
#         if myresult[i][0] not in applied:
#             print(myresult[i][0] + " " + myresult[i][1] + " " + myresult[i][2])
#
#
