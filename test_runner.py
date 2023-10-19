# import pytest
# import mysql
# #from register import new_password_check
# from welcome import welcome
# from io import StringIO
# from register import new_password_check
# from register import number_of_account_check
# from valid_major_list import valid_major_list
# from collections import defaultdict
# from help_center import help_center
# from about import about
# from press import press
# from last_applied import last_applied
# from blog import blog
# from careers import careers
# from developers import developers
# from browse_incollege import browse_incollege
# from business_solutions import business_solutions
# from directories import directories
# from guest_controls import guest_controls
# # from friend_list import show_friends
# from friends_requests import delete_request
# from messages import show_all_messages
# from register import new_member_notification
# from post_job import new_job_notification
# import unittest.mock as mock
#
#
# @pytest.yield_fixture
# def fake_input():
#     with mock.patch('input') as m:
#         yield m
#
#
# def test_displayLoginMenu(capsys):
#     with mock.patch('builtins.input', return_value='1'):
#         welcome()
#
#
# def test_new_password_check():
#     Valid_Pwds = ["Test123@", "Testing1234@"]
#     for pwd in Valid_Pwds:
#         assert new_password_check(pwd) == True
#
#     Invalid_Pwds = ["Test123", "test123@", "Test@One"]
#     for pwd in Invalid_Pwds:
#         assert new_password_check(pwd) == False
#
#
# # def test_number_of_account_check():
# #     count = 0
# #     Num_Users = open("userInfo.txt", "r")
# #     for user in Num_Users:
# #         count += 1
# #     if count < 10:
# #         assert number_of_account_check(Num_Users)
#
#
# def test_valid_major_list():
#     Valid_Majors = [
#         "Computer Science", "Computer Engineering", "Political Science",
#         "Biochemistry", "Biomedical Engineering", "Sports Management"
#     ]
#     assert valid_major_list() == Valid_Majors
#     Invalid_Majors = [
#         "Marketing", "Communications", "Music", "Health Sciences"
#     ]
#     assert valid_major_list() != Invalid_Majors
#
#
# def test_helpCenter(capsys):
#     with mock.patch('builtins.input', return_value='1'):
#         help_center()
#
#
# def test_about(capsys):
#     with mock.patch('builtins.input', return_value='1'):
#         about()


# def test_press(capsys):
#     with mock.patch('builtins.input', return_value='1'):
#         press()


#def test_guestControls (capsys):
#with mock.patch('builtins.input', return_value='1'):
#cursor = capsys
#assert cursor.execute('SELECT * FROM guest_table') == "off"

#def test_search_user(capsys):
#with mock.patch('builtins.input', return_value='1'):
#search_user()
# mydb = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="welcome1",
#     database="InCollege"
# )
#
# cursor = mydb.cursor(buffered=True)

# def test_add_friends():
#     person1 = "juan"
#     person2 = "pedro"
#     assert add_friends(person1, person2) == "successful"


# def test_remove_friends():
#     person1 = "juan"
#     person2 = "pedro"
#     friends = defaultdict(list)
#     friends[person1].append(person2)
#     friends[person2].append(person1)
#     friends[person1].remove(person2)
#     assert friends == {'juan': [], 'pedro': ['juan']}

#
# def test_show_friend_list():
#     assert show_friends() == "[]"


# def test_delete_request():
#     assert delete_request()

# def test_show_all_messages():
#     assert show_all_messages()

# def test_account_type():
#     new_username = "lulu33"
#     new_password = "Loop3888!"
#     new_first_name = "Lauren"
#     new_last_name = "France"
#     university = "Ithaca College"
#     major = "Computer Science"
#     title = "4th year Computer Science student"
#     lang = "English"
#     account_type = "Plus"
#
#     cursor.execute(
#         "INSERT INTO userInfo (username, Password, FirstName, LastName, University, Major, Title, Language,account_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)",
#         (new_username, new_password, new_first_name, new_last_name, university, major, title, lang, account_type))
#     mydb.commit()
#
#     command = ("SELECT username, Password, FirstName, LastName, University, Major, Title, Language,account_type  FROM userInfo WHERE username = %s")
#     args = (command, new_username )
#     cursor.execute(command)
#     result_table = cursor.fetchall()
#     print(result_table)


# def new_member_notif_test():

    # assert new_member_notification("paul", "Bell", "pBell")

    # cursor.execute("Select notification FROM skwilliams1_notification WHERE read_status = 1")

# def test_job_notif():
#
#     assert new_job_notification("Scientist")

# def test_last_applied():
#     assert last_applied()