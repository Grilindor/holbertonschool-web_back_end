#!/usr/bin/env python3
""" 9. Insert a document in Python """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The keyword arguments representing the document to insert.

    Returns:
        The _id of the newly created document.
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
