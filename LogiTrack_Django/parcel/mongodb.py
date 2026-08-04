from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://anjali:anju123@logitrackcluster.mmp2qke.mongodb.net/?retryWrites=true&w=majority&appName=LogiTrackCluster"
)

db = client["logitrack_db"]

parcel_collection = db["parcels"]