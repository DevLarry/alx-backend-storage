#!/usr/bin/env python3
"""List all with python"""


def list_all(mongo_collection):
    """My list"""
    return mongo_collection.find()
