#!/usr/bin/env python3
"""
adding the top 10 of the most present IPs in the collection nginx
of the database logs
"""

import pymongo


def log_stats(mongo_collection):
    """
    function to collect the log stats
    and calculate them
    """
    try:
        # Calculate the number of logs
        num_logs = mongo_collection.count_documents({})

        # Aggregate to get method counts and top IPs
        pipeline = [
            {"$group": {"_id": "$method", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
            {"$project": {"_id": 0, "method": "$_id", "count": 1}}
        ]
        method_counts = list(mongo_collection.aggregate(pipeline))

        pipeline = [
            {"$group": {"_id": "$clientIP", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
            {"$project": {"_id": 0, "clientIP": "$_id", "count": 1}}
        ]
        ip_counts = list(mongo_collection.aggregate(pipeline))

        # Print the number of logs and method counts
        print(f"{num_logs} logs")
        print("Methods:")
        for method in method_counts:
            print(f"    {method['method']}: {method['count']}")

        # Print the top IPs
        print("IPs:")
        for ip in ip_counts:
            print(f"     {ip['clientIP']}: {ip['count']}")

    except pymongo.errors.PyMongoError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        # Connect to the MongoDB database and collection
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["logs"]
        logs = db["nginx"]

        # Call the log_stats function
        log_stats(logs)
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")
