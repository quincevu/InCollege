def general():
    print("Select an option below: ")
    print("1. Sign up")
    print("2. Help center")
    print("3. About")
    print("4. Press")
    print("5. Blog")
    print("6. Careers")
    print("7. Developers")
    print("8. Back to Useful Links")
    print("9. Back to home")

    selection = input()
    option_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while selection not in option_list:
        selection = input("Invalid option. Please choose again: ")

    if selection == "1":
        return "register"
    if selection == "2":
        return "help_center"
    if selection == "3":
        return "about"
    if selection == "4":
        return "press"
    if selection == "5":
        return "blog"
    if selection == "6":
        return "careers"
    if selection == "7":
        return "developers"
    if selection == "8":
        return "useful_links"
    if selection == "9":
        return "home"