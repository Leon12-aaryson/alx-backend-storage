#!/usr/bin/env python3
'''
    This script defines a Python function that inserts a new document
    into a collection based on keyword arguments.

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object.
    Returns the new _id.
'''

import pymongo

def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document into the collection.

    :param mongo_collection: pymongo collection object
    :param kwargs: key-value pairs representing the document to be inserted
    :return: the new _id of the inserted document
    '''
    return mongo_collection.insert(kwargs)

