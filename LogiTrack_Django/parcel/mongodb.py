import os
from pymongo import MongoClient

_client = None
_db = None


def get_db():
    global _client, _db

    if _db is None:
        mongo_uri = os.environ.get("MONGO_URI")

        if not mongo_uri:
            return None

        _client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000
        )

        db_name = os.environ.get(
            "MONGO_DB_NAME",
            "logitrack_db"
        )

        _db = _client[db_name]

    return _db


def get_parcel_collection():
    db = get_db()

    if db is None:
        return None

    return db["parcels"]


def get_user_collection():
    db = get_db()

    if db is None:
        return None

    return db["users"]