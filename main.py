# import pytest
import mysql.connector
from outputAPI import output_api
from studentAccountAPI import StudentAccountAPI

#from replit import db
#pytest.main
#to be used for assertations in pytest
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
# cursor.execute("UPDATE userInfo SET inSession = 0 where username = 'skwilliams1'")
# cursor.execute("UPDATE userInfo SET inSession = 0 where username = 'shaderr' ")
# cursor.execute("DELETE FROM userInfo")
# # creating database
cursor.execute("CREATE DATABASE IF NOT EXISTS InCollege")
 # cursor.execute("CREATE DATABASE InCollege")

# create table for userInfo
cursor.execute("CREATE TABLE IF NOT EXISTS userInfo (username VARCHAR(30) NOT NULL, PRIMARY KEY (username),FirstName VARCHAR(100) NULL, "
                 "LastName VARCHAR(100) NULL, password VARCHAR(12) NULL, Major VARCHAR (45) NULL, Title VARCHAR (200) NULL,"
                 "University VARCHAR(100) NULL, Description VARCHAR (100) NULL, Education VARCHAR(50) NULL, Language VARCHAR (100) NULL, "
                 "inSession INTEGER(1) NULL, account_type VARCHAR (100) NULL);")
# add inSession in column
# cursor.execute("ALTER TABLE userInfo ADD inSession INTEGER(1) NULL")11
# cursor.execute ("ALTER TABLE userInfo ADD account_type VARCHAR(100) NULL")
# create table for friends
cursor.execute("CREATE TABLE IF NOT EXISTS Friend"
               "(FriendID INTEGER AUTO_INCREMENT, "
               "Username VARCHAR(30) NOT NULL REFERENCES username,"
               "Username2 VARCHAR(30) NOT NULL REFERENCES username,"
               "CONSTRAINT pks PRIMARY KEY (FriendID))")


# create table for friend request
cursor.execute("CREATE TABLE IF NOT EXISTS friendRequests"
               "(friendRequestID INTEGER AUTO_INCREMENT,"
               "Account1 VARCHAR(30) NOT NULL,"
               "Account2 VARCHAR(30) NOT NULL,"
               "CONSTRAINT RequestPKS PRIMARY KEY (friendRequestID))")
# cursor.execute("ALTER TABLE friendRequests DROP FOREIGN KEY Account1 REFERENCES username")


cursor.execute("CREATE TABLE IF NOT EXISTS message"
               "(mesageID INTEGER AUTO_INCREMENT,"
               "Sender VARCHAR(30) NOT NULL,"
               "Receiver VARCHAR(30) NOT NULL,"
               "userMessage VARCHAR(100) NOT NULL,"
               "read_status BOOLEAN,"
               "CONSTRAINT RequestPKS PRIMARY KEY (mesageID))")


#create table for job
cursor.execute("CREATE TABLE IF NOT EXISTS Jobs"
               "(Username VARCHAR (30) NOT NULL,"
               "Title VARCHAR (50) NULL,"
               "Employer VARCHAR (100) NULL,"
               "StartDate VARCHAR (100) NULL,"
               "EndDate VARCHAR (100) NULL,"
               "Location VARCHAR (200) NULL,"
               "Description VARCHAR (500) NULL)")

#create table for job posting
cursor.execute("CREATE TABLE IF NOT EXISTS Job1"
              "(JobID INTEGER AUTO_INCREMENT,"
               "username VARCHAR (50) NULL,"
               "Title VARCHAR (50) NULL,"
               "PosterName VARCHAR (250) NULL,"
               "Employer VARCHAR (100) NULL,"
               "Salary Integer NULL,"
               "Location VARCHAR (200) NULL,"
               "Description VARCHAR (500) NULL,"
                "PRIMARY KEY (JobID))")

#cursor.execute("DROP TABLE Job1")

#create table for job
cursor.execute("CREATE TABLE IF NOT EXISTS JobsApplied"
               "(Username VARCHAR (30) NOT NULL,"
               "savedJobs VARCHAR (100) NULL,"
               "appliedJobs VARCHAR (100) NULL,"
               "Title VARCHAR (50) NULL,"
               "gradDate VARCHAR (50) NULL,"
               "startDate VARCHAR (50) NULL,"
               "Reason VARCHAR (500) NULL,"
               "deletedJobs INTEGER NULL,"
               " InDtTm DATETIME DEFAULT CURRENT_TIMESTAMP)")

# cursor.execute("ALTER TABLE JobsApplied ADD Title VARCHAR (50) NULL")

mydb.close()
if __name__ == "__main__":
    from driver import driver
    StudentAccountAPI()
    output_api()
    driver()
