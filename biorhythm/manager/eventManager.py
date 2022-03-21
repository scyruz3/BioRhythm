from typing import List
from bson import ObjectId
from biorhythm.dao import eventDAO
import datetime

def getEventsCreatedByUser(userId: ObjectId) -> List[dict]:
    createdEvents = eventDAO.getEventsCreatedByUser(userId=userId)
    return createdEvents


def getConfirmedEventsByUser(userId: ObjectId) -> List[dict]:
    confirmedEvents = eventDAO.getConfirmedEventsByUser(userId=userId)
    return confirmedEvents


def getPendingEventsByUser(userId: ObjectId) -> List[dict]:
    pendingEvents = eventDAO.getPendingEventsByUser(userId=userId)
    return pendingEvents

def postEvent(newEvent):
    eventTime = datetime.datetime.strptime(newEvent['eventTime'], '%H:%M').time()
    eventDate = datetime.datetime.strptime(newEvent['eventDate'], '%Y-%m-%d')
    newEvent['eventDate'] = datetime.datetime.combine(eventDate, eventTime)
    newEvent = eventDAO.postNewEvent(event=newEvent)
    return newEvent
