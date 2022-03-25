from validation import *
from user_operations import*
from login import login 

def register():
   
   
    firstname = input("please enter your first name :-")
    if firstname.isalpha():
        second_name = check_second_name()
        email = check_email()
        phone = check_phone()
        password = check_password()
        parameters = [firstname+",", second_name +
                      ",", email+",", phone+",", password+","]
        adding_info = add_user(parameters)
        if adding_info:
            print("user add successfully")
            print ("please login to your account ")
            login()
         
    else:
        print(" name should contain letters only")
        register()
