from welcome import welcome
import sqlite3

def languages():
    connection = sqlite3.connect("my_database")
    connection.execute("CREATE TABLE IF NOT EXISTS lang_table (lang STRING);")
    connection.execute("INSERT INTO lang_table(lang) ""VALUES ('english')")

# Read
    cursor_object = connection.execute("SELECT * FROM lang_table")
   
    
      #  english=True;#having the default english value be true and if the user chooses to turn off the feature changing it to false that way this can be read by the system as false and it has been "changed" to spanish by the system
    print("Would you like to switch to Spanish")
    print("1. Yes")
    print("2. No")

    
    option = input()
    option_list = ["1", "2"]
    while option not in option_list:
        option = input("Invalid option, please try again: ")
        
    if option == "1":
        #english=False;
        #connection.execute("DELETE from project_table WHERE lang='spanish';")
        connection.execute("UPDATE lang_table SET lang = 'Spanish' WHERE lang='english'")
        print("switching to spanish")
        connection.commit()
        #print(cursor_object.fetchall())
        

    elif option == "2":
        return "welcome"


       