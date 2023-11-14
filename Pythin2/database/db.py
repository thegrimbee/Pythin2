from pymongo import MongoClient
import hashlib
import os
from dotenv import load_dotenv
import secrets

# Load .env file
dotenv_path = dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path)

# Emails
pythin20001_email = "Pythin2.0001@gmail.com"


class Database:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client.get_database(db_name)

    def get_collection(self, collection_name):
        return self.db[collection_name]

class UserDatabase(Database):
    def __init__(self):
        print("UserDatabase initializing...")
        super().__init__('mongodb://localhost:27017/', 'user_db')
        self.users = self.db.get_collection("users")
    
    def user_exists(self, username):
        print("Checking if user exists...")
        return self.users.find_one({"username": username}) != None
    
    def register_user(self, username, password, email):
        print("Creating user...")
        if self.user_exists(username):
            print("User already exists")
            return False
        else:
            print(f"{username} registered")
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.users.insert_one({"username": username, 
                                   "password": hashed_password, 
                                   "email": email, 
                                   "verified": False,
                                   "verification_code": secrets.token_hex(10),
                                   "unattempted": [i for i in range(1, 21)],
                                   "attempted": [],
                                   "passed": []})
            return True

    def verify_check(self, username):
        print(f"Checking if {username} is verified...")
        return self.users.find_one({"username": username})["verified"]
    
    def verify_user(self, code):
        print("Verifying user...")
        user = self.users.find_one({"verification_code": code})
        if user != None:
            self.users.update_one({"verification_code": code}, {"$set": {"verified": True}, "$unset": {"verification_code": ""}})
            return True
        else:
            return False
        
    def login_user(self, username, password):
        print("Logging in user...")
        if self.user_exists(username):
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return self.users.find_one({"username": username, "password": hashed_password}) != None
        else:
            print("User does not exist")
            return False
    
    def display_users(self):
        print("Displaying users...")    
        for user in self.users.find():
            print(user)
    
    def update_level_status(self, username, level_num, status):
        print("Updating level status...")

        if status == "attempted":
            unattempted = self.users.find_one({"username": username})["unattempted"]
            attempted = self.users.find_one({"username": username})["attempted"]
            attempted.append(unattempted.pop(level_num))
            self.users.update_one({"username": username}, {"$set": {"unattempted": unattempted, "attempted": attempted}})
        elif status == "passed":
            attempted = self.users.find_one({"username": username})["attempted"]
            passed = self.users.find_one({"username": username})["passed"]
            passed.append(attempted.pop(level_num))
            self.users.update_one({"username": username}, {"$set": {"attempted": attempted, "passed": passed}})
        else:
            print("Invalid status")
            return False
        
        print("Level status updated")
        return True

user_db = UserDatabase()
user_db.display_users()