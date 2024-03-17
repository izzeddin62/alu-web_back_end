#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def main():
    """ log stats"""
    try:
        with MongoClient() as client:
            client = MongoClient()
            db = client.logs
            logs = db.nginx

            num_logs = logs.count_documents({})
            methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
            results = [0, 0, 0, 0, 0]
            num_status_check = logs.count_documents({"method": "GET", "path": "/status"})
            for method in methods:
                num_method = logs.count_documents({"method": method})
                results[methods.index(method)] = num_method
            
            print("{} logs".format(num_logs))
            print("Methods:")
            for method in methods:
                print("\tmethod {}: {}".format(method, results[methods.index(method)]))
            
            print("{} status check".format(num_status_check))
    except Exception as e:
        print("there was an error")




if __name__ == "__main__":
    main()
