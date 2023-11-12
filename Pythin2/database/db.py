from pymongo import MongoClient
import hashlib

class Database:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client.get_database(db_name)

    def get_collection(self, collection_name):
        return self.db[collection_name]

class UserDatabase(Database):
    def __init__(self):
        print("UserDatabase initializing...")
        super().__init__('mongodb://localhost:27017', 'user_db')
        self.users = self.get_collection("users")
    
    def user_exists(self, username):
        print("Checking if user exists...")
        return self.users.find_one({"username": username}) != None
    
    def create_user(self, username, password):
        print("Creating user...")
        if self.user_exists(username):
            print("User already exists")
            return False
        else:
            print("User added to database")
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.users.insert_one({"username": username, "password": hashed_password})
            return True

    def login_user(self, username, password):
        print("Logging in user...")
        if self.user_exists(username):
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return self.users.find_one({"username": username, "password": hashed_password}) != None
        else:
            print("User does not exist")
            return False

user_db = UserDatabase()