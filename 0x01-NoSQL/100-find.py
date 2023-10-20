#!/usr/bin/env python3
"""100-find"""
import sys
from pymongo import MongoClient

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} ARG".format(sys.argv[0]))
        exit(1)

    client = MongoClient('mongodb://localhost:27017/')
    db = client[sys.argv[1]]
    collection = db['school']
    documents = collection.find({'name': {'$regex': '^Holberton'}})

    for document in documents:
        print(document)
