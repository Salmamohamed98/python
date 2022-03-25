from login_operations import*
import sys


def add_user(parameters):
    id = get_last_user_id()
    parameters.append(str(id))
    users_files = open("users.txt", "a+")
    users_files.writelines("\n")
    users_files.writelines(parameters)
    users_files.close()
    id = parameters[-1]
    f = open(f'{id}.json', 'w')
    f.write("{\"projects\":[]}")
    return "added"


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


###########################################



