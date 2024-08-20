#!/usr/bin/env python3
""" 11. Where can I learn Python? """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ list of schools that have the topic in their topics array. """
    return mongo_collection.find({"topics": topic})
