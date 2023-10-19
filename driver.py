from mapper import run_current_status


def driver():
    current_status = "welcome"
    while current_status != 666:
        current_status = run_current_status(current_status)
    print("Program exited successfully. Bye bye!")
