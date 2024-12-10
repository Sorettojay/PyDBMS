import csv
import os

c = os.getcwd() + " \ ".strip()
d = os.getcwd() + " \ ".strip() + "Test.db"
e = os.getcwd() + " \ ".strip() + "Test.db" + " \ ".strip() + "b.txt"
print(c)
print(len(os.listdir(d)))
#os.remove(d)
#os.rmdir(d)
