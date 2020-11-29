import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_docs = [{"first": "terry",
             "last": "pratchett",
             "dob": "28/04/1948",
             "gender": "m",
             "hair_color": "not much",
             "occupation": "writer",
             "nationality": "british"},
            {"first": "george",
             "last": "rr martin",
             "dob": "20/09/1948",
             "gender": "m",
             "hair_color": "white",
             "occupation": "writer",
             "nationality": "american"},
            ]

# Insert Many
coll.insert_many(new_docs)

# Find all
documents = coll.find()

# Find specific records, ie first nme of douglas
documents = coll.find({"first": "douglas"})

# Remove specific records
coll.remove({"first": "douglas"})

# Update first record with nationality american
coll.update_one({"nationality": "american"},
                {"$set": {"hair_color": "maroon"}})

# Update all records with nationality american
coll.update_many({"nationality": "american"},
                 {"$set": {"hair_color": "maroon"}})

# Print all records in db
for doc in documents:
    print(doc)
