import re
import json

##########################################


def get_project(id, title):
    file = open(f"{id}.json", "r")
    data = json.load(file)["projects"]
    for dict in data:
        if dict["Title"] == f"{title}":
            return data.index(dict), data

    return -1,data
        
    

####################################################


def get_title(id):
    title = input("please enter project title :")
    if title != "":
        if get_project(id, title):
            print("project exist please enter different title")
            return get_title(id)

        else:
            return title
    else:
        print("title cannot be empty")
        return get_title(id)

###############################################################


def get_details():
    det = input("please enter project details :")
    if det != "":
        return det
    else:
        return get_details()

#################################################################


def get_total_target():
    try:
        target = int(input("please enter your total target :"))

        return target
    except:
        print("total target should be numbers only ")
        return get_total_target()

#####################################################################


def get_start_date():
    print("please enter starting date for your project :")
    print("imp: date should be in the form of dd/mm/yyyy")
    date = input("")
    d_pattern = re.search(
        "^(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$", date)
    if d_pattern:
        return date
    else:
        return get_start_date()

####################################################################################


def get_end_date():
    print("please enter ending date for your project :")
    print("imp: date should be in the form of dd/mm/yyyy")
    date = input("")
    d_pattern = re.search(
        "^(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$", date)
    if d_pattern:
        return date
    else:
        return get_start_date()

###########################################################################################
