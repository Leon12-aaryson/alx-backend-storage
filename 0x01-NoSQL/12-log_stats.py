#!/usr/bin/env python3
"""
Write a Python script that provides some stats about
    Nginx logs stored in MongoDB
"""
import pymongo
from pymongo import MongoClient


def print_nginx_stats(nginx_logs):
    ''' function that gives stats about Nginx logs '''
    print(f"{nginx_logs.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = nginx_logs.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")


if __name__ == "__main__":
    nginx_logs = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    print_nginx_stats(nginx_logs)
