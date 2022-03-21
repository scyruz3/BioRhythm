from typing import List
from biorhythm import mongo
from bson import ObjectId, json_util
import json

db = mongo.db


def getEventsCreatedByUser(userId: ObjectId) -> List[dict]:
    query = {"creator": str(userId)}
    # process cursor data type
    createdEvents = json.loads(json_util.dumps(db.Events.find(query)))
    return createdEvents


def getConfirmedEventsByUser(userId: ObjectId) -> List[dict]:
    query = {"confirmedUsers": str(userId)}
    confirmedEvents = json.loads(json_util.dumps(db.Events.find(query)))
    return confirmedEvents


def getPendingEventsByUser(userId: ObjectId) -> List[dict]:
    query = {"invitedUsers": str(userId)}
    pendingEvents = json.loads(json_util.dumps(db.Events.find(query)))
    return pendingEvents

def postNewEvent(event) -> bool:
    db.Events.insert_one({
        'creator': event['creator'], 
        'title': event['title'], 
        'description': event['description'], 
        'biorhythmType':event['biorhythmType'],
        'confirmedUsers': [],
        'eventDate': event['eventDate'],
        'invitedUsers': event['invitedUsers']
        })
        
    return 0