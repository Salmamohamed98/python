from user_operations import *


def check_existance(email: str):
    f = open("users.txt", "r")
    l = 0
    while(l) != "":
        l = f.readline()
        Line = l.split(",")
        if email in Line:
            break

    else:
        return True

    f.close()
    return False
#############################


def check_phone_existance(phone: str):
    f = open("users.txt", "r")
    l = 0
    while(l) != "":
        l = f.readline()
        Line = l.split(",")
        if phone in Line:
            break

    else:
        return True

    f.close()
    return False
#####################################


def login_credintial(email, password):
    f = open("users.txt", "r")

    l = 0
    while(l) != "":
        l = f.readline()
        if l == "\n":
            continue
        else:
            Line = l.split(",")
            if email in Line:
                if password in Line:
                    id = Line[-1]
                    return "user exist", id
                else:

                    return "wrong password", "-1"
    f.close()
    return "Email doesn't exist","-1"
