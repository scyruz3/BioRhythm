import string
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
    newEvent = db.Events.find_one({
        'creator': event['creator'], 
        'title': event['title'], 
        'description': event['description'], 
        'biorhythmType':event['biorhythmType'],
        'eventDate': event['eventDate'],
        }) 
    return newEvent['_id']

def getEventbyEventId(eventId: ObjectId):
    event = db.Events.find_one({"_id": ObjectId(eventId)})
    return event

def updateEvent(eventId: ObjectId, newValues)-> bool:
    db.Events.update_one({'_id': eventId}, {'$set': {
        'title': newValues['title'], 
        'description': newValues['description'], 
        'biorhythmType':newValues['biorhythmType'],
        'eventDate': newValues['eventDate']
    }})
    return 0

def un_inviteFriend(eventId: ObjectId, newList)-> bool:
    db.Events.update_one({'_id': ObjectId(eventId)}, {'$set': {'invitedUsers': newList}})
    return newList