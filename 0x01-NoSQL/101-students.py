#!/usr/bin/env python3
"""
module that deals with returning results of students
average in a python funtion
"""

from pymongo import MongoClient
from collections import namedtuple


def top_students(mongo_collection):
    # Aggregation pipeline to calculate the average score for each student
    # and sort the results in descending order of average score
    result = mongo_collection.aggregate([
        {"$match": {"type": "student"}},  # Filter for student documents
        {"$group": {
            "_id": "$name",
            "totalScore": {"$sum": "$score"},
            "numTests": {"$sum": 1}
        }},
        {"$project": {
            "_id": 0,
            "name": "$_id",
            "averageScore": {"$divide": ["$totalScore", "$numTests"]}
        }},
        {"$sort": {"averageScore": -1}}
    ])

    """Convert the results to a list of namedtuples, each containing
    the student's name and average score"""
    return [namedtuple('Student', 'name averageScore')(*x) for x in result]
