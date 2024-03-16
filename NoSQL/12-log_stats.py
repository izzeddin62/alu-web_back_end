#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient



def get_logs(logs):
    num_docs = logs.count_documents({})
    docs = list(logs.find())
    print(f"{num_docs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_method = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {num_method}")

    filter_path = {"method": "GET", "path": "/status"}
    num_path = logs.count_documents(filter_path)
    print(f"{num_path} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    get_logs(logs)

