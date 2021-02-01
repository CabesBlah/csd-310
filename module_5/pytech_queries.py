#Caleb Lewandowski
#February 1, 2021
#Module 5.3 Assignment

#Set up connection.
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.lwbyv.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

#Display all student data.
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"])
    print()

#Display one set of student data.
print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id":1007})
print("Student ID:", doc["student_id"])
print("First Name:", doc["first_name"])
print("Last Name:", doc["last_name"])
print()

input("\n\nEnd of program, press any key to exit...")