#!/usr/bin/env python3
'''
    This script defines a Python function that lists all
    documents in a collection.

    Prototype: def list_all(mongo_collection):
    Returns an empty list if no documents are found in the collection.
    mongo_collection will be the pymongo collection object.
'''

import pymongo

def list_all(mongo_collection):
    '''
    Lists all documents in the collection.

    :param mongo_collection: pymongo collection object
    :return: list of all documents in the collection, or an empty list if no documents are found
    '''
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [doc for doc in documents]
