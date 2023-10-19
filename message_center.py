from messages import show_all_messages
from messages import show_unread_messages


def message_center():
    print("Welcome to your message center! Please choose an option below: ")
    print("1. View new messages\n2. View all messages\n3. Back to home page")
    selection = input()
    option = ["1", "2", "3"]
    while selection != "3":
        while selection not in option:
            selection = input("Invalid option, please try again: ")
        if selection == "1":
            show_unread_messages()
            print("Please choose an option below:\n1. View new messages\n2. View all messages\n3. Back to home page")
            selection = input()
            continue
        if selection == "2":
            show_all_messages()
            print("Please choose an option below:\n1. View new messages\n2. View all messages\n3. Back to home page")
            selection = input()
            continue
    return "home"
