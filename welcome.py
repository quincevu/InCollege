def welcome():  #hash = 0
    print(
        "Welcome to InCollege! Thousands of College students are landing jobs and networking. Select an option below to get started."
    )
    print("1. Log in")
    print("2. Register")
    print("3. Watch a story")
    print("4. Find someone I might know")
    print("5. Useful Links")
    print("6. Quit InCollege")
    option = input()
    option_list = ["1", "2", "3", "4", "5","6"]
    while option not in option_list:
        option = input("Invalid option, please try again: ")
    if option == "1":
        return "login"
    if option == "2":
        return "register"
    if option == "3":
        return "see_the_story"
    if option == "4":
        return "find_member"
    if option == "5":
        return "useful_links"
    if option == "6":
        return 666
