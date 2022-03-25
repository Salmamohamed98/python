import re
from user_existance import*


def check_email():
    email = input("please enter valid  email:- ")
    e_pattern = re.search("@.*\.com$", email)
    if not e_pattern:
        print("it's not a valid email\n ")
        return check_email()
    else:
        if check_existance(email):
            return email
        else:
            print("user email already exist enter different email ")
            return check_email()

##########################


def check_phone():

    phone = input("please enter valid phone number :-")
    try:
        x = int(phone)
        p_pattern = re.findall("^01[0-2]", phone)
        length = len(phone)
        if length == 11 and p_pattern:
            if check_phone_existance(phone):
                return phone
            else:
                print("user phone already exist enter different phone")
                return check_phone()
        else:
            print("it's not a valid phone number\n")
            return check_phone()
    except:
        print("please enter phone number without letters")
        return check_phone()
##########################################


def check_second_name():
    second_name = input("please enter your second name :-")
    if second_name.isalpha():
        return second_name

    else:
        print("please enter name with letters only")
        return check_second_name()
#########################################


def check_password():

    password = input("please enter a password more than 4 characters :- ")
    if len(password) < 4:
        print(" week password try again ")
        check_password()
    else:
        return confirm_password(password)


###########################################

def confirm_password(entered_password: str, i=0):

    if (i >= 3):
        print("maximum number of confirmation error you need to enter new one")
        check_password()
    else:
        c_password = input("please confirm entered password")
        if c_password == entered_password:
            return entered_password
        else:
            print("not match try again")
            i += 1
            return confirm_password(entered_password, i)

# 3############################ 33


def get_last_user_id():
    with open("users.txt", "r") as f:
        try:
            last_line = f.readlines()[-1]
            id = last_line.split(",")[-1]
            id = int(id)
            id += 1
        except:
            id = 1
    f.close()
    return id
