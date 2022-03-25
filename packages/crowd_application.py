
from registeration import register
from login import login


def start_program():

    start = input(
        "please enter number of  your choice :-\n 1) Register 2) Login \n")
    if start == "1":
        register()
    elif start == "2":
        login()
    else:
        print("bad choice")
        


# calling
start_program()
