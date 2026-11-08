from pymongo import MongoClient

# connection to the actual database, link is to where it lives on the pc
client = MongoClient("mongodb://localhost:27017")

# we are specifying which of our possibly many databases we are using in this app
db = client["toka"]

# we are getting specific collections we have, so other files can import and use them
users = db["users"]

# OPTIONAL, ONLY IF YOU TRULLY CAN'T HAVE DUPLICATE VALUES
users.create_index("email", unique=True)





