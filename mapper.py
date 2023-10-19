from home import home
from welcome import welcome
from login import login
from register import register
from see_the_story import see_the_story
from find_job import find_job
from post_job import post_job
from find_member import find_member
from learn_new_skill import learn_new_skill
from useful_links import useful_links
from general import general
from browse_incollege import browse_incollege
from business_solutions import business_solutions
from directories import directories
from help_center import help_center
from about import about
from press import press
from blog import blog
from careers import careers
from developers import developers
from incollege_important_links import incollege_important_links
from friend_list import show_friends
from Student_Profile import show_profile
from Jobs_InputAPI import Jobs_API
from find_job import all_jobs
'''In the future, I want to see a directory containing all the functional files, which allows us to just import the whole
directory instead of every signle file there. That will make short work of this. maybe when i'm back to the dev 
position, i will do that.'''


def run_current_status(current_status):
    # process the hashed returned current status here with all the if statements
    # name of functions must be identical to the return value for safety during development process
    # in local functional files, DO NOT return another function for the response; we do not want to load the RAM/call
    # stack up with just function calls
    # read the home.py file, which is written 100% by #me, so that you understand how this system works.
    # if you have questions, ask me. if you simply do not trust me, just copy my methods and don't even question it.
    # i have put everything yall did before the implementation of this system in a file called main_reserved.txt
    # because they are no longer needed for operation.
    # i will not delete them, i will let yall do that yourselves if you wish.

    if current_status == "welcome":
        return welcome()
    if current_status == "home":
        return home()
    if current_status == "login":
        return login()
    if current_status == "register":
        return register()
    if current_status == "see_the_story":
        return see_the_story()
    if current_status == "find_job":
        return find_job()
    # if current_status == "post_job":
    #     return post_job()
    if current_status == "post_job":
        return post_job()
    if current_status == "find_member":
        return find_member()
    if current_status == "learn_new_skill":
        return learn_new_skill()
    if current_status == "useful_links":
        return useful_links()
    if current_status == "general":
        return general()
    if current_status == "browse_incollege":
        return browse_incollege()
    if current_status == "business_solutions":
        return business_solutions()
    if current_status == "directories":
        return directories()
    if current_status == "help_center":
        return help_center()
    if current_status == "about":
        return about()
    if current_status == "press":
        return press()
    if current_status == "blog":
        return blog()
    if current_status == "careers":
        return careers()
    if current_status == "developers":
        return developers()
    if current_status == "incollege_important_links":
        return incollege_important_links()
    if current_status == "friend_list":
        return show_friends()
    if current_status == "show_friends":
        return show_friends()
    if current_status == "show_profile":
        return show_profile()
    if current_status == "Jobs_API":
        return Jobs_API()
    all_jobs()
