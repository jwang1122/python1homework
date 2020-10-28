from pymongo import MongoClient
import uuid

# CRUD: Create, Retrieve, Update, Delete

students = {
    "_id": uuid.uuid4().hex,
    "name": "Evan Xiao",
    "age": 10,
    "grade": 5,
    "score": 100,
    "gender": "male"
}

client = MongoClient('mongodb://localhost:27017')
db = client['mydb']
studentsdb = db.students

result = studentsdb.insert_one(students)
print(result.inserted_id)