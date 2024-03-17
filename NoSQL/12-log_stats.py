#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def main():
    """ log stats"""
    with MongoClient() as client:
        client = MongoClient()
        db = client.logs
        logs = db.nginx

        num_logs = logs.count_documents({})
        print("{} logs".format(num_logs))
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            num_method = logs.count_documents({"method": method})
            print("\tmethod {}: {}".format(method, num_method))

        num_status_check = logs.count_documents({"method": "GET", "path": "/status"})
        print("{} status check".format(num_status_check))




if __name__ == "__main__":
    main()
