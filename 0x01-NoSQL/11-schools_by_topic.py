#!/usr/bin/env python3
'''
module that lists schools havingg specific topics
'''

import pymongo


def schools_by_topic(mongo_collection, topic):
    '''
    function that returns the list of school having a specific topic:
    '''
    try:
        # Find schools that have the specified topic
        matching_schools = mongo_collection.find({"topics": topic})

        # Extract school names from the matching documents
        school_names = [school["name"] for school in matching_schools]

        return school_names

    except pymongo.errors.PyMongoError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        # Connect to the MongoDB database and collection
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["school"]
        schools = db["schools"]

        # Example usage: find schools by topic
        topic_to_search = "Mathematics"
        matching_schools = schools_by_topic(schools, topic_to_search)
        if matching_schools:
            print(f"Schools offering '{topic_to_search}':")
            for school in matching_schools:
                print(school)
        else:
            print(f"No schools found offering '{topic_to_search}'.")

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")
