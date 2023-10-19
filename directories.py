def directories():
    print("Page under construction!")
    selection = input("Please select an option below: ")
    print("1. Return to Useful Links")
    print("2. Return to Home")
    option_list = ["1", "2"]
    while selection not in option_list:
        selection = input("Invalid option. Please choose again: ")
    if selection == "1":
        return "useful_links"
    if selection == "2":
        return "home"