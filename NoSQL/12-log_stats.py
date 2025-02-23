#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        db = client.logs
        nginx_collection = db.nginx

        # Check if collection is empty
        n_logs = nginx_collection.count_documents({})
        if n_logs == 0:
            print("No logs found. Inserting sample data...")
            sample_data = [
                {"method": "GET", "path": "/home"},
                {"method": "POST", "path": "/submit"},
                {"method": "GET", "path": "/status"},
                {"method": "PUT", "path": "/update"},
                {"method": "DELETE", "path": "/remove"},
                {"method": "PATCH", "path": "/modify"},
                {"method": "GET", "path": "/data"},
                {"method": "POST", "path": "/api"},
                {"method": "GET", "path": "/check"},
                {"method": "GET", "path": "/logs"}
            ]
            nginx_collection.insert_many(sample_data)
            n_logs = nginx_collection.count_documents({})  # Update log count

        # Print log count
        print(f'{n_logs} logs')

        # Count and display method usage
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print('Methods:')
        for method in methods:
            count = nginx_collection.count_documents({"method": method})
            print(f'\tmethod {method}: {count}')

        # Count GET requests to /status
        status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
        print(f'{status_check} status check')

    except Exception as e:
        print(f"Error: {e}")