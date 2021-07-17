import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URL = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "bully"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URL)

coll = conn[DATABASE][COLLECTION]

new_docs = [{
    "first": "dona",
    "last": "bully",
    "dob": "08/04/2021",
    "gender": "f",
    "hair_color": "red",
    "nationality": "irish"
},{
    "first": "alek",
    "last": "bully", 
    "dob": "08/04/2021",
    "gender": "m",
    "hair_color": "red",
    "nationality": "irish"
},{
    "fisrt": "lina",
    "last": "bully",
    "dob": "08/04/2021",
    "gender": "f",
    "hair_color": "red",
    "nationality": "irish"
},{
    "fisrt": "Mic",
    "last": "bully",
    "dob": "08/04/2021",
    "gender": "m",
    "hair_color": "red",
    "nationality": "irish"
},{
    "fisrt": "lina",
    "last": "bully",
    "dob": "08/04/2021",
    "gender": "f",
    "hair_color": "red",
    "nationality": "irish"
},{  
    "fisrt": "lina",
    "last": "bully",
    "dob": "08/04/2021",
    "gender": "f",
    "hair_color": "red",
    "nationality": "irish"
}]

documents = coll.find()

for doc in documents:
    print(doc)
