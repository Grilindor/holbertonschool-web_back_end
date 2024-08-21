#!/usr/bin/env python3
"""
nginx_stats.py
A script that provides statistics about Nginx logs stored in a MongoDB database.
"""
from pymongo import MongoClient


def main():
    """print the stats of logs Nginx stoked in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        m_count = collection.count_documents({"method": method})
        print(f"\tmethod{method}: {m_count}")

    stat_check_count = collection.count_documents({"method": "GET",
                                                   "path": "/status"})
    print(f"{stat_check_count} status check")


if __name__ == "__main__":
    main()
