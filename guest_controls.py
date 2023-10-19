import sqlite3
def guest_controls():
  
       # incollege_emails=True; #having the default value be true and if the user chooses to turn off the feature changing it to false that way this can be read by the system as false
        #incollege_sms=True;
        #incollege_adv=True;

        connection = sqlite3.connect("my_database")
        connection.execute("CREATE TABLE IF NOT EXISTS guest_table (emails STRING, sms STRING, adv STRING);")
        connection.execute("INSERT INTO guest_table (emails,sms,adv) "
             "VALUES ('on', 'on','on')")

# Read
        cursor_object = connection.execute("SELECT * FROM guest_table")
   
        print("1. Turn Off Incollege Emails")
        print("2. Turn Off Incollege SMS")
        print("3. Turn Off Incollege Advertising Features")

        option = input()      
        option_list = ["1", "2", "3"]
        while option not in option_list:
          option = input("Invalid option, please try again: ")

        if option =="1":
          #incollege_emails = False;
          connection.execute("UPDATE guest_table SET emails = 'off' WHERE emails='on'")
          print("You will not receive any more emails")
          connection.commit()
          #print(cursor_object.fetchall())

        elif option == "2":
         # incollege_sms=False;
          connection.execute("UPDATE guest_table SET sms = 'off' WHERE sms='on'")
          connection.commit()
          #print(cursor_object.fetchall())
          print("You will not recieve any more SMS")

        elif option == "3":
          #incollege_adv=False;
          connection.execute("UPDATE guest_table SET adv = 'off' WHERE adv='on'")
          connection.commit()
          print("You will not recieve any more advertisement features")
         