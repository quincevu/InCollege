def press():
    print(
        "In College Pressroom: Stay on top of the latest news, updates and reports"
    )
    selection = input()
    option_list = ["1", "2"]
    while selection not in option_list:
        selection = input("Invalid option. Please choose again: ")
    if selection == "1":
        return "general"
    if selection == "2":
        return "home"