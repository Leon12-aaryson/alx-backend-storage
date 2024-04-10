#!/usr/bin/env python3
'''
module deals with getting schools with specific topics
'''

import pymongo


def update_topics(mongo_collection, name, topics):
    '''
    function to collect schools with specific topics
    '''
    try:
        # Update the topics for the specified school name
        mongo_collection.update_many({"name": name},
                                     {"$set": {"topics": topics}})
        print("Topics updated successfully.")

    except pymongo.errors.PyMongoError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        # Connect to the MongoDB database and collection
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["school"]
        schools = db["schools"]

        # Example usage: update topics for a school
        school_name = "Example School"
        new_topics = ["Mathematics", "Science", "History"]
        update_topics(schools, school_name, new_topics)

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")
