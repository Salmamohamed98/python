import email
import re
from user_existance import *
from validation import*
from user_operations import *


def enter_email():
    email = input("please enter valid  email:- ")
    e_pattern = re.search("@.*\.com$", email)
    if not e_pattern:
        print("it's not a valid email\n ")
        return enter_email()
    else:
        return email


def enter_password():
    password = input("please enter a password more than 4 characters :- ")
    if len(password) < 4:
        print(" week password try again ")
        return check_password()
    else:
        return password





def login():
    email = enter_email()
    password = enter_password()
    result, id = login_credintial(email, password)
    id = id.replace("\n", "")
    match result:
        case "user exist":
            options(menu(), id)
        case "wrong password":
            print("wrong password")
            login()
        case "Email doesn't exist":
            print("Email doesn't exist")
            login()
