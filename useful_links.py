def useful_links():
    print("Select an option:")
    print("1. General")
    print("2. Browse Incollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Back to home")

    selection = input()
    option_list = ["1", "2", "3", "4", "5"]
    while selection not in option_list:
        selection = input("Invalid option, please choose again: ")

    if selection == "1":  #done
        return "general"
    if selection == "2":
        return "browse_incollege"
    if selection == "3":
        return "business_solutions"
    if selection == "4":
        return "directories"
    if selection == "5":
        return "home"
