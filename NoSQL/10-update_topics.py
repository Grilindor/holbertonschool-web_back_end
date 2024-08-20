#!/usr/bin/env python3
""" 10. Change school topics """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ updat a collection in python """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )
