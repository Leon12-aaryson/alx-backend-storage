#!/usr/bin/env python3
'''
module deals with getting schools with specific topics
'''

import pymongo


def update_topics(mongo_collection, name, topics):
    '''
    function to collect schools with specific topics
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
