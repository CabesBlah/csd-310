#Caleb Lewandowski
#February 5, 2021
#Module 6.2 Assignment

#Set up connection.
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.lwbyv.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

#Display data of all students.
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"])
    print()

#Update data of Student 1007.
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name":"Beep"}})

#Display data of Student 1007.
print("\n-- DISPLAYING STUDENT DOCUMENT 1007 --")
doc = db.students.find_one({"student_id":"1007"})
print("Student ID:", doc["student_id"])
print("First Name:", doc["first_name"])
print("Last Name:", doc["last_name"])
print()

input("\n\nEnd of program, press any key to exit...")