from welcome import welcome
from guest_controls import guest_controls
from languages import languages


def incollege_important_links():
    print("Select an option:")
    print("1. Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. Languages")
    print("10.Quit")
  
    #selection = input()
    option = input()
    option_list = ["1", "2", "3", "4", "5","6","7","8","9","10"]
    while option not in option_list:
        option = input("Invalid option, please try again: ")

    if option == "1":
     print("To view our copyright notice please click on this link ") 
     copyright_notice = 'https://www.disclaimergenerator.net/live.php?token=0aTe6XfZOQC3AjqABSgVNHkRUFTqRrry'
     print(copyright_notice)

    elif option == "2":
     print("inCollege brings economic opportunity for every member of the global workforce. At inCollege we strive to help connect the students in college to make them more productive and successful! ")

    elif option == "3":
     print("To view our Accessibilty please click on this link ") 
     Accessibilty = 'file:///C:/Users/prern/Downloads/accessibility-statement_2022-09-07.html'
     print(Accessibilty) 

    elif option == "4":
     print("To view our user agreement please click on this link ") 
     user_agreement = 'https://www.privacypolicies.com/live/a2a33717-2a11-4213-beea-1690724c551b'
     print(user_agreement)

      #number 5 is at the end

    elif option == "6":
       print ("To view our cookie policy please click on this link ")
       cookie_policy= 'https://www.termsfeed.com/live/3e24d3af-2d0f-4050-9d88-4a34454381f5' 
       print(cookie_policy)

    elif option == "7":
       print("To view our copyright policy please click on this link ") 
       copyright_policy = 'https://www.privacypolicies.com/live/21fdec5d-bc68-4e71-815a-f031e31907a7'
       print(copyright_policy)

    elif option == "8":
       print("To view our brand policy please click on this link ") 
       brand_policy = 'https://www.privacypolicies.com/live/fafaf432-64c8-4936-8e73-f9f91d06207d'
       print(brand_policy)

    elif option == "9":  
      return languages() 
      
    elif option == "5":
      
      print("Would you like to see Guest controls?")
      print("1. Yes")
      print("2. No")

      option = input()
      option_list = ["1", "2"]
      while option not in option_list:
        option = input("Invalid option, please try again: ")
        
      if option == "1":
        return guest_controls() 
        
      elif option == '2':
        return incollege_important_links()

    elif option =="10":
        return "welcome"
  
  
        
     
        
