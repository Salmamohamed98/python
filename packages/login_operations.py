import json
from project_info import *
import sys

#########################


def menu():
    print("chooese number of what you want to do ")
    choice = input(
        "1)view projects  2) create project  3)delete project \n 4)search with title 5) edit project 6)exit \n")
    return choice


def options(choice, id):
    match choice:
        case "1":
            view(id)
        case "2":
            create(id)

        case "3":
            delete(id)
        case "4":
            search(id)
        case "5":
            ediit(id)
        case "6":
            sys.exit()

####################################


def view(id: str):
    projects = open(f"{id}.json")
    data = json.load(projects)
    for i in data['projects']:
        print(json.dumps(i, sort_keys=False, indent=4))
    projects.close()
    x = input("if you eant to back to menu press m or any letter to exit:-")
    if x == "m":
        return options(menu(),id)
    else:
        sys.exit()

###############################


def append_new(list, id):
    with open(f"{id}.json", "w") as f:
        json.dump(list, f)

#####################################################


def create(id: str):

    with open(f"{id}.json") as np:

        listObj = json.load(np)
        temp = listObj["projects"]
        temp.append(
            {
                "Title": f"{get_title(id)}",
                "Details": f"{get_details()}",
                "Total Target": f"{get_total_target()}",
                "Start date": f"{get_start_date()}",
                "End date": f"{get_end_date()}"
            }
        )

    append_new(listObj, id)
    x = input("if you eant to back to menu press m or any letter to exit:-")
    if x == "m":
       return options(menu(), id)
    else:
        sys.exit()

#############################################


def remove(indx, id):

    with open(f"{id}.json") as np:

        listObj = json.load(np)
        temp = listObj["projects"]
        temp.pop(indx)

    append_new(listObj, id)


def delete(id):

    title = input("please enter project title to be deleted")
    if title != "":
        indx, data = get_project(id, title)
        if indx!=-1:
            remove(indx, id)
            return options(menu(), id)

        else:
            x = input(
                "project doesn't exist press c to try again or any key to  back to menu ")
            if x == "c":
                delete(id)
            else:
               return options(menu(), id)

##############################################


def search(id):

    title = input("please enter project title to search")
    if title != "":

        indx, data = get_project(id, title)
        if indx!=-1:
            print(json.dumps(data[indx], sort_keys=False, indent=4))
            return options(menu(), id)
        else:
            x = input(
                "project doesn't exist press c to try again or any key to  menu ")
            if x == "c":
                search(id)
            else:
               return options(menu(), id)
####################################################


def edit(key, value, id, o_title):

    with open(f"{id}.json") as np:
        listObj = json.load(np)
        temp = listObj["projects"]
        for dict in temp:
            if dict["Title"] == o_title:
                dict[key] = value
        append_new(listObj, '1')
        x = input("enter  e to back to edit or any other letter to exit")
        if x == "e":
            ediit(id)
        else:
            sys.exit()


def ediit(id):
    o_title = input("please enter project title you want to edit")
    indx, data = get_project(id, o_title)
    if indx!=-1:

        print(" please enter number of what you to edit :")
        x = input(
            "1)Title  2)Details  3)Total Target 4) Start date  5)End date ")
        match x:
            case "1":
                edit("Title", get_title(), id, o_title)
            case "2":
                edit("Details", get_details(), id, o_title)
            case "3":
                edit("Total target", get_total_target(), id, o_title)
            case "4":
                edit("Start date", get_start_date(), id, o_title)
            case "5":
                edit("End date", get_end_date(), id, o_title)
            case _:
                print("error input ")
                ediit(id)
    else:
        x = input(
            "project doesn't exist press c to try again or any key to  back to menu ")
        if x == "c":
            ediit(id)
        else:
           return options(menu(), id)
