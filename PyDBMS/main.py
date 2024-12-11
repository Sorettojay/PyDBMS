import os

import Commands
import User_Prompts
import Tokenizer

def intro_prompt():
    print("")
    print("Welcome to PyDBMS! To exit, type in 'exit'.")
    print("Press 1 to log in.")
    print("Press 2 to Create an Account.")
    print("Press 3 for developer mode.")
    option = input("Enter a response here: ")

    if option == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username is not None and password is not None:
            user = User_Prompts.login_info_prompt(username, password)
            if user is True:
                return True
            else:
                print("")
                __main__()
        else:
            print("")
            __main__()

    if option == "2":
        User_Prompts.add_login_info_prompt()
        intro_prompt()

    if option == "3":
        return True

    if option == "Exit" or option == "exit" or option == "EXIT":
        return

    intro_prompt()

def Database_Management_System(account_validator: True):
    conn = Commands.Connection()
    while account_validator is True:
        query = input()
        if query == "Exit" or query == "exit" or query == "EXIT":
            return
        query = Tokenizer.Tokenize(query)
        if len(query) == 1:
            print("Error: Invalid user query")

        """
        Handling CREATE statements
        """
        if query[0] == "CREATE":
            query.pop(0)
            if query[0] == "DATABASE":
                query.pop(0)
                Commands.Database().create_database(query)
            if query[0] == "TABLE":
                query.pop(0)
                Commands.Table().create_table(query)
            if query[0] == "CONNECTION":
                query.pop(0)
                conn.create_connection(query)

        """
        Handling DELETE Statements
        """
        if query[0] == "DELETE":
            query.pop(0)
            if query[0] == "DATABASE":
                query.pop(0)
                Commands.Database().delete_database(query)

        """
        Handling SHOW Statements
        """
        if query[0] == "SHOW":
            query.pop(0)
            databases = []
            if query[0] == "DATABASES":
                for i in os.listdir(os.getcwd()):
                    if ".db" in i:
                        databases.append(i)
                print(databases)
            if query[0] == "CONNECTIONS":
                pass


def __main__():
    account_validator = intro_prompt()
    if account_validator is True:
        print("")
        User_Prompts.table_prompt()
        Database_Management_System(account_validator)
    else:
        print("Account could not be validated")
        print("Exiting Database Management System")

__main__()