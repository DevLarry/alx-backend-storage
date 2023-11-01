#!/usr/bin/env python3
"""
find by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find by topic
    """
    return mongo_collection.find({"topics": topic})
