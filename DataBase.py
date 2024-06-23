from pymongo import MongoClient
import Config
from tkinter import messagebox

DBURL = Config.DataBaseURL

try:
    # Connect to MongoDB
    client = MongoClient(DBURL)
    db = client["Bank-System"]
    AdminDB = db["Administration"]
    CustomerDB = db["Customers"]
    
    # Check if the connection is successful
    if client is not None and db is not None:
        print("Connected to MongoDB successfully!")
        # Now you can perform further operations with AdminDB and CustomerDB
    else:
        print("Failed to connect to MongoDB!")
        messagebox.showerror("DataBase Failed", "Failed to connect to MongoDB!. Please check configuration and try again.")
        
except Exception as e:
    print("An error occurred:", str(e))
    messagebox.showerror(f"DataBase Failed", "An error occurred: {e}")


