#Caleb Lewandowski
#February 1, 2021
#Module 5.3 Assignment

#Set up connection.
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.lwbyv.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

#Insert student data.
print("-- INSERT STATEMENTS --")
new_student_object = {"student_id":1007, "first_name":"Bob", "last_name":"Bank"}
new_student_id = students.insert_one(new_student_object).inserted_id
print("Inserted student record", new_student_object["first_name"], new_student_object["last_name"], "into the students collection with document_id", new_student_id)
new_student_object = {"student_id":1008, "first_name":"Dude", "last_name":"Done"}
new_student_id = students.insert_one(new_student_object).inserted_id
print("Inserted student record", new_student_object["first_name"], new_student_object["last_name"], "into the students collection with document_id", new_student_id)
new_student_object = {"student_id":1009, "first_name":"Where", "last_name":"What"}
new_student_id = students.insert_one(new_student_object).inserted_id
print("Inserted student record", new_student_object["first_name"], new_student_object["last_name"], "into the students collection with document_id", new_student_id)

input("\n\nEnd of program, press any key to exit...")