import mysql.connector
import os.path

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="welcome1",
    database="InCollege"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT username FROM userinfo WHERE inSession = 1")
userinfo = mycursor.fetchall()
if len(userinfo) != 0:
    userName = userinfo[0][0]

def Jobs_API():
    f_in = os.path.exists('newJobs.txt')
    
    f_in = open('newJobs.txt', 'r')
    clean = f_in.readlines()
    tmp = ''
    output = []

    for i in clean:
        if '=====' in i: # means next job so reset
            output.append(tmp)
            tmp = ''
            continue

        if '&&&' in i: 
            continue

        tmp += i

    output.append(tmp) # for last job
    # fields = {}
    # title=output[0]
    # poster_name=output[1]
    # employer_name=output[2]
    # salary=output[3]
    # location=output[4]
    # description=output[5]
    
    for i in range(len(output)):
        idx = 0
        fields={}
        for j in output[i].split('\n'):
            fields[idx] = j
            idx += 1
        #func with logic to get jobs from db
        title=fields[0]
        poster_name=fields[1]
        employer_name=fields[2]
        salary=fields[3]
        location=fields[4]
        description=fields[5]
        post_job_from_API(title, poster_name, employer_name, salary, location, description)
        fields.clear()


    print(fields)
    print(output)
    return output

def post_job_from_API(title_in , posterName_in, employer_in, salary_in, location_in, description_in):
    mycursor.execute("SELECT COUNT(*) from Job1")
    result = mycursor.fetchone()
    print(result)
    if result[0] >=10:
        print("Job capacity is full")

    else:  # redundant condition check
        # print("Enter job:")
        # title_in = input("Title:")
        # posterName_in = input("Poster Name:")
        # description_in = input("Description:")
        # employer_in = input("Employer:")
        # location_in = input("Location: ")
        # salary_in = input("salary:")

        # Jobs_API()
        mycursor.execute(
            "INSERT INTO Job1 (Title, PosterName, Employer, Salary, Location, Description, userName)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (title_in , posterName_in, employer_in, salary_in, location_in, description_in, userName))
        # new_job_notification(title_in)
        mydb.commit()
    return "home"

