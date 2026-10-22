from pymongo import MongoClient


#connection to database, link to where it is within the pc
client = MongoClient(
    "mongodb://localhost:27017"
)

#specified which of many databases are being used within this app
db = client["ToKa-Database"]

#gets access to specific collections so other files and operations can be done
users = db["users"]

#only used if you cant have duplicate values
users.create_index("email", unique=True)