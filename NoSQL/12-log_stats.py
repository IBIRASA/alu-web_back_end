#!/usr/bin/env python3
"""Python script to analyze Nginx logs in MongoDB"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """Provides stats about Nginx logs stored in MongoDB"""
    # Get the total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")

    # Count the number of logs for each HTTP method
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of logs with method=GET and path="/status"
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    # Call the log_stats function
    log_stats(nginx_collection)
