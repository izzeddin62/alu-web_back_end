#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def main():
    """ log stats"""
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        db = client.logs
        logs = db.nginx

        num_logs = logs.count_documents({})
        print(f"{num_logs} logs")
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            num_method = logs.count_documents({"method": method})
            print(f"\tmethod {method}: {num_method}")

        num_status_check = logs.count_documents({"method": "GET", "path": "/status"})
        print(f"{num_status_check} status check")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
