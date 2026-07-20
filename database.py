from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create Database
db = client["logitrack_db"]

# Create Collection
parcels = db["parcels"]
users = db["users"]

print("MongoDB Connected Successfully!")