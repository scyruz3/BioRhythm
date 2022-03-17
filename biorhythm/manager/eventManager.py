from typing import List
from bson import ObjectId
from biorhythm.dao import eventDAO


def getEventsCreatedByUser(userId: ObjectId) -> List[dict]:
    createdEvents = eventDAO.getEventsCreatedByUser(userId=userId)
    return createdEvents


def getConfirmedEventsByUser(userId: ObjectId) -> List[dict]:
    confirmedEvents = eventDAO.getConfirmedEventsByUser(userId=userId)
    return confirmedEvents


def getPendingEventsByUser(userId: ObjectId) -> List[dict]:
    pendingEvents = eventDAO.getPendingEventsByUser(userId=userId)
    return pendingEvents
