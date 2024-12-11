"""
Commands.py
"""
import csv
import os

class Connection:
    """
    A class to create an object that connects to other databases
    """
    def __init__(self):
        self.connection = [] #A list to hold connections to databases

    def create_connection(self, query: list):
        """
        Creates a connection to a database

        :param query:
        :return:
        """
        database = os.getcwd() + " \ ".strip() + query[0] #path to the database
        if os.path.exists(database):
            self.connection.append(database)
        else:
            print("Connection with database could not be established.")
            print("Please recheck the name of your database.")

    def show_connections(self, query: list):
        """
        Lists all the current database connections
        
        :param query:
        :return:
        """
        print(self.connection)

class Database:
    """
    Class structure for Database Objects
    """
    def __init__(self):
        self.name = ""
        self.directory = os.getcwd() + " \ ".strip()
        self.tables = os.listdir(self.directory)

    def create_database(self, query: list):
        """
        Creates an instance of a database object and a ".db" folder

        :param query: The query typed in from the user
        :return: A database object instance
        """
        self.name = query[0]
        query.pop(0)
        if os.path.exists(self.directory + self.name + ".db"):
            print("Database already exists. Please name the database something else.")
        else:
            os.mkdir(self.name+".db")
        return self

    def list_tables(self):
        """
        Lists all tables contained in the database

        :param query: The query type in from the user
        :return: Returns nothing
        """
        print(os.listdir(self.directory))
        return

    def delete_database(self, query: list):
        self.name = query[0]
        if len(os.listdir(self.directory + self.name + ".db")) > 0:
            print("Error: Database is not empty.")
        elif os.path.exists(self.directory + self.name + ".db") is None:
            print("Database does not exist")
        else:
            os.rmdir(self.directory + self.name + ".db")
        return

class Table:
    """
    Class structure for holding Table Objects
    """
    def __init__(self):
        self.name = ""
        self.db = ""
        self.cols = []
        self.rows = []

    def create_table(self, query: list):
        """
        Creates a table instance

        :param query: The query a user types in
        :return: Returns an instance of a table object
        """
        self.name = query[0]
        query.pop(0)
        if query[0] == "(":
            while query[0] != ")":
                if query[0] == ")":
                    break
                self.cols.append(query.pop(0))

        return self

    def delete(self):
        pass

    def insert(self, query: list):
        pass
        if len(self.rows) != len(self.rows):
            print("Error: Columns and Rows are mismatched.")

    def select(self, query):
        pass

    def update(self):
        pass

    def view(self):
        pass

