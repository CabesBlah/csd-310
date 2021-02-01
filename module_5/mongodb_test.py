#Caleb Lewandowski
#January 31, 2021
#Module 5.2 Assignment

#Set up connection.
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.lwbyv.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#List collections in database.
print("-- Pytech Collection List --")
print(db.list_collection_names())

input("\n\n  End of program, press any key to exit...")