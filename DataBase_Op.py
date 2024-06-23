
from DataBase import AdminDB,CustomerDB

def Check_for_matches(Search_Query, DbName):
    if DbName == "CustomerDB":
        result = CustomerDB.find_one(Search_Query)
    elif DbName == "AdminDB":
        result = AdminDB.find_one(Search_Query)
    else:
        print("No DB Named with that name!")
    return result is not None



def Add_Remove_Admin(Email, flag):
    if flag == "add":
        AdminDB.update_one({}, {"$push": {"Admin Users": {"$each": [Email]}}})
        print(f"{Email} user added to administrator") 
    elif flag == "remove":
        AdminDB.update_one({}, {"$pull": {"Admin Users": Email}})
        print(f"{Email} user removed from administrator")
    else:
        print("Invalid flag provided. Please provide either 'add' or 'remove'.")

def Check_admin_user(user):
    AdminDOcs=AdminDB.find_one({})
    if user in AdminDOcs.get("Admin Users", []):
        return AdminDOcs.get("Admin Users", [])
    else:
        return False




def Insert_Customer_Data(Data):
    CustomerDB.insert_one(Data)
    print("Data inserted successfully")
    

