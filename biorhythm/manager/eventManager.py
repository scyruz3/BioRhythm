from typing import List
from bson import ObjectId
from biorhythm.dao import eventDAO


def getEventsCreatedByUser(userId: ObjectId) -> List[dict]:
    createdEvents = eventDAO.getEventsCreatedByUser(userId=userId)
    return createdEvents
