from incollege_important_links import incollege_important_links
from friend_list import show_friends
from Student_Profile import show_profile
from search_user import search_user
from friends_requests import friend_requests
from logout import logout
from post_job import del_or_post
from messages import check_unread_messages
from message_center import message_center
from Student_Profile import check_profile
from last_applied import last_applied
from notification import show_new_notification
from find_job import all_jobs
from find_job import jobs_applied
from find_job import jobs_saved

def home():
    if check_unread_messages():
        print("You have messages waiting for you")
    if check_profile():
        print("Don't forget to create a profile")
    # last_applied()
    show_new_notification()

    print("Welcome back! Please select an option below.")
    print("1. Explore open positions")
    print("2. Post a job")
    print("3. Learn a new skill")
    print("4. Log out")
    print("5. InCollege Important Links")
    print("6. See Network")
    print("7. Search user")
    print("8. View pending requests")
    print("9: Profile")
    print("10. Message center")
    print("11. Quit InCollege")
    option = input("Please choose an option above (1-10) :")
    option_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    while option not in option_list:
        option = input("Invalid option, please choose again!")
    if option == "1":
        return "find_job"
    if option == "2":
        return del_or_post()
    if option == "3":
        return "learn_new_skill"
    if option == "4":
        logout()
        return "welcome"
    if option == "5":
        return incollege_important_links()
    if option == "6":
        return "show_friends"
    if option == "7":
        return search_user()
    if option == "8":
        return friend_requests()
    if option == "9":
        return "show_profile"
    if option == "10":
        return message_center()
    if option == "11":
        all_jobs()
        jobs_applied()
        jobs_saved()
        return 666

    # all_jobs()
#We need a "setting" option to change password, first and last name, and even username, or to delete the account. Ask me if you don't know how to do it.
