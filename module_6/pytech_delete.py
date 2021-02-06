#Caleb Lewandowski
#February 5, 2021
#Module 6.3 Assignment
#Purpose: To demonstrate deleting student data.

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

#Create student data.
student_carrot = {
	"student_id":"1010",
	"first_name":"Carrot",
	"last_name":"Coral",
	"enrollments": [{
		"term":"Summer",
		"gpa":"3.2",
		"start_date":"6/1/2019",
		"end_date":"8/28/2019",
		"courses":[{
			"course_id":"23456",
			"description":"Java 101",
			"instructor":"Someone Important",
			"grade":"C+"
		}]
    }]
}

#Insert student data.
print("\n-- INSERT STATEMENTS --")
new_student_id = students.insert_one(student_carrot).inserted_id
print("Inserted student record into the students collection with document_id", str(new_student_id))

#Display one set of student data.
print("\n-- DISPLAYING STUDENT TEST DOC --")
doc = db.students.find_one({"student_id":"1010"})
print("Student ID:", doc["student_id"])
print("First Name:", doc["first_name"])
print("Last Name:", doc["last_name"])
print()

#Delete student data.
students.delete_one({"student_id":"1010"})

#Display all student data.
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"])
    print()

input("\n\nEnd of program, press any key to exit...")