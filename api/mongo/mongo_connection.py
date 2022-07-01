from hashlib import new
import motor.motor_asyncio
from bson.objectid import ObjectId

#Connection
MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection("students_collection")

url_database = client.urls
url_collection = url_database.get_collection("url_collection")

access_log_database = client.access_logs
access_log_collection = access_log_database.get_collection("access_log_collection")

#Helpers
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }

def url_helper(url) -> dict:
    return {
        "id": str(url["_id"]),
        "url_short": url["url_short"],
        "url_long": url["url_long"],
        "creation_time": url["creation_time"],
    }

def access_log_helper(access_log) -> dict:
    return {
        "_id": str(access_log["_id"]),
        "url_id": access_log["url_id"],
        "device": access_log["device"],
        "ip": access_log["ip"],
        "location": access_log["location"],
        "creation_time": access_log["creation_time"],
    }

# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True

# Add a new url into to the database
async def add_url(url_data: dict) -> dict:
    url = await url_collection.insert_one(url_data)
    new_url = await url_collection.find_one({"_id": url.inserted_id})
    return url_helper(new_url)
"""
# Retrieve a url with a matching ID #62bdf28005afc7764cfc82ab
async def retrieve_url(id: str) -> dict:
    url = await url_collection.find_one({"_id": ObjectId(id)})
    if url:
        return url_helper(url)
"""
# Retrieve a url with a matching short URL
async def retrieve_url_short(id: str) -> dict:
    url = await url_collection.find_one({'url_short': id })
    if url:
        return url_helper(url)

# Add a new access log into to the database
async def add_access_log(access_log_data: dict) -> dict:
    access_log = await access_log_collection.insert_one(access_log_data)
    new_access_log = await access_log_collection.find_one({"_id": access_log.inserted_id})
    return access_log_helper(new_access_log)

# Retrieve all access logs present in the database
async def retrieve_access_logs():
    access_logs = []
    async for access_log in access_log_collection.find():
        access_logs.append(access_log_helper(access_log))
    return access_logs

# Retrieve id from short URL
async def retrieve_id(id: str):
    id = await url_collection.find_one({'url_short': id })
    if id:
        return url_helper(id)['id']
    return None

# Retrieve dates for URL
async def retrieve_dates(id: str):
    dates = await access_log_collection.aggregate([
        { '$match': { 'url_id': id } },
        { '$group': {
        '_id': {
            '$dateToString': {
                'date': { '$toDate': "$creation_time" }, 'format': "%Y-%m-%d" } },
                'n': { '$sum': 1 }
        } },
        { '$sort' : { '_id' : 1 } }
    ]).to_list(length=None)
    return dates

# Retrieve dates for URL
async def retrieve_devices(id: str):
    devices = await access_log_collection.aggregate([
        { '$match': { 'url_id': id } },
        { '$group': {
        '_id': '$device',
	      'n': { '$sum': 1}}
        },
        { '$sort' : { '_id' : 1 } }
    ]).to_list(length=None)
    return devices

# Retrieve locations for URL
async def retrieve_locations(id: str):
    locations = await access_log_collection.aggregate([
        { '$match': { 'url_id': id } },
        { '$group': {
        '_id': '$location',
	      'n': { '$sum': 1}}
        },
        { '$sort' : { '_id' : 1 } }
    ]).to_list(length=None)
    return locations