from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.lwbyv.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
print("-- Pytech Collection List --")
print(db.list_collection_names())
input("\n\nEnd of program, press any key to exit...")