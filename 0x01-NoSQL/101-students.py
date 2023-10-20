#!/usr/bin/env python3
"""101-students"""


def top_students(mongo_collection):
    """ function that returns all students sorted by average score:"""
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
