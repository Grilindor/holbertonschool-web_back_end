#!/usr/bin/env python3
""" 8. List all documents in Python """
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection, or an empty list if none.
    """
    doc = mongo_collection.find()
    return list(doc)
