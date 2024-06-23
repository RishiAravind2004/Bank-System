import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://copycat-devloperz:chipi-chipi@cluster0.zcqzk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Update with your MongoDB URI
db = client['mydatabase']  # Update with your database name
collection = db['mycollection']  # Update with your collection name

# Retrieve data from MongoDB
data = list(collection.find())

# Convert data to DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)
