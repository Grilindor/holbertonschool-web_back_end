#!/usr/bin/env python3
""" 10. Change school topics """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    doc_updeted = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )
    return doc_updeted
