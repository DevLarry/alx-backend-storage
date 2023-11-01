#!/usr/bin/env python3
"""Insert document"""


def insert_school(mongo_collection, **kwargs):
    """Insert a documnent into the database"""
    return mongo_collection.insert_one(kwargs).inserted_id
