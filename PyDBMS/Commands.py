"""
Commands.py
"""
import csv
import os

class Database:
    """
    Class structure for Database Objects
    """
    def __init__(self):
        self.name = ""
        self.directory = os.getcwd() + " \ ".strip() + self.name
        self.tables = os.listdir(self.directory)

    def create_database(self, query: list):
        """
        Creates an instance of a database object and a ".db" folder

        :param query: The query typed in from the user
        :return: A database object instance
        """
        self.name = query[0]
        query.pop(0)
        if os.path.exists(self.directory+".db"):
            print("Database already exists. Please name the database something else.")
            return
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

    def delete_database(self):
        if len(os.listdir(self.directory)) > 0:
            print("Error: Database is not empty.")
        else:
            os.rmdir(self.directory)
        return


class Table:
    """
    Class structure for holding Table Objects
    """
    def __init__(self):
        self.name = ""
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

