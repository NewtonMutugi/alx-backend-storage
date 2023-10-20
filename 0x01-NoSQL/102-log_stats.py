#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    logs_collection = client.logs.nginx

    # Total number of logs
    total_logs = logs_collection.count_documents({})

    # Number of logs by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        method_counts[method] = count

    # Number of logs by status code
    status_counts = {}
    for log in logs_collection.find():
        status = log.get("status")
        if status:
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

    # Top 10 IPs by number of logs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = logs_collection.aggregate(pipeline)

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{sum(status_counts.values())} status check")
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
