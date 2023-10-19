def help_center():
    print("We are here to help!\n")
    print("Please select an option below: ")
    print("1. Return to General")
    print("2. Return to Home")
    selection = input()
    option_list = ["1", "2"]
    while selection not in option_list:
        selection = input("Invalid option. Please choose again: ")
    if selection == "1":
        return "general"
    if selection == "2":
        return "home"