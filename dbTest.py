from pymongo import MongoClient


    # Connect to MongoDB
client = MongoClient("mongodb+srv://copycat-devloperz:chipi-chipi@cluster0.zcqzk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Bank-System"]
AdminDB = db["Administration"]
CustomerDB = db["Customers"]

Administration = {
    "Configuration": {
        "Interest": None
    },
    "Admin Users": [],
    "Logs": []
}

AdminDB.insert_one(Administration)

print("Database structure created successfully.")
