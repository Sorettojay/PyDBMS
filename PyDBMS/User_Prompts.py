"""
User facing functions that the user uses to interact with the database
"""
import csv

def add_login_info_prompt():
    username = input("Please add your desired username: ")
    with open("login_info.csv", 'r', newline='') as file:
        row = csv.reader(file, delimiter=',')
        for word in row:
            if username == word:
                print("This username is already taken. Please type in another username.")
                add_login_info_prompt()
    password = input("Please type in your password: ")
    password_2 = input("Retype your password: ")
    if password != password_2:
        print("Your passwords did not match. The prompt will restart once more.")
        add_login_info_prompt()
    with open("login_info.csv", 'a', newline='') as file:
        row = csv.writer(file, delimiter=',')
        row.writerow([username, password])
    print("Your account has been made. You will be returned back to the introduction screen.")

def login_info_prompt(username, password):

    with open("login_info.csv", 'r') as file:
        row = csv.reader(file)

        for i in row:
            if username in i:
                if password in i:
                    print(f"Access Granted! Welcome to PyDBMS {username}!")
                    return True
                else:
                    print("The password you have entered does not match our records.")
                    return False

        print("The username you have entered is not found. Please try again.")
        return False

def table_prompt():
    print("**************************************************************")
    print("You are now in the table editor. Write a query to get started!")
    print("Press 1 to list databases")
    print("Press 2 to list tables")
    print("**************************************************************")





