#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient


if __name__ == "__main__":
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://localhost:27017')
    logs = client.logs.nginx
    print("{} logs".format(logs.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(method, logs.count_documents(
            {"method": method})))
    print("{} status check".format(logs.count_documents(
        {"method": "GET", "path": "/status"})))
