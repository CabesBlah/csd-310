#Caleb Lewandowski
#February 1, 2021
#Module 5.3 Assignment

#Set up connection.
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.lwbyv.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

#Create student data.
student_bob = {
	"student_id":"1007",
	"first_name":"Bob",
	"last_name":"Bank",
	"enrollments": [{
		"term":"Summer",
		"gpa":"4.0",
		"start_date":"6/1/2019",
		"end_date":"8/28/2019",
		"courses":[{
			"course_id":"23456",
			"description":"Java 101",
			"instructor":"Someone Important",
			"grade":"A"
	    }]
    }]
}

student_dude = {
	"student_id":"1008",
	"first_name":"Dude",
	"last_name":"Done",
	"enrollments": [{
		"term":"Summer",
		"gpa":"3.5",
		"start_date":"6/1/2019",
		"end_date":"8/28/2019",
		"courses":[{
			"course_id":"23456",
			"description":"Java 101",
			"instructor":"Someone Important",
			"grade":"A-"
		}]
    }]
}

student_where = {
	"student_id":"1009",
	"first_name":"Where",
	"last_name":"What",
	"enrollments": [{
		"term":"Summer",
		"gpa":"3.0",
		"start_date":"6/1/2019",
		"end_date":"8/28/2019",
		"courses":[{
			"course_id":"23456",
			"description":"Java 101",
			"instructor":"Someone Important",
			"grade":"B"
		}]
    }]
}

#Insert student data.
print("-- INSERT STATEMENTS --")

new_student_id = students.insert_one(student_bob).inserted_id
print("Inserted student record", student_bob["first_name"], student_bob["last_name"], "into the students collection with document_id", new_student_id)

new_student_id = students.insert_one(student_dude).inserted_id
print("Inserted student record", student_dude["first_name"], student_dude["last_name"], "into the students collection with document_id", new_student_id)

new_student_id = students.insert_one(student_where).inserted_id
print("Inserted student record", student_where["first_name"], student_where["last_name"], "into the students collection with document_id", new_student_id)

input("\n\nEnd of program, press any key to exit...")