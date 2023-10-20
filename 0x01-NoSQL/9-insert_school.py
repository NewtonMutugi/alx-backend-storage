#!/usr/bin/env python3
"""9-insert_school"""


def insert_school(mongo_collection, **kwargs):
    """"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
