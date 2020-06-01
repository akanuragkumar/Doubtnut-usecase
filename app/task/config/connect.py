from pymongo import MongoClient


def mongo_connect():
    mongodb_host = 'localhost'
    mongodb_port = 27017
    client = MongoClient(mongodb_host, mongodb_port)
    db = client.yourdb
    return db
