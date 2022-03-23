from pickle import OBJ
from typing import List
from webbrowser import get
from bson import ObjectId
import biorhythm
from biorhythm.dao import eventDAO, userDAO
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


def getEvent(eventId: ObjectId):
    event = eventDAO.getEventbyEventId(eventId)
    event = {
        "title": event["title"],
        "description": event["description"],
        "eventDate": str(event["eventDate"].year)
        + "-"
        + "{:02d}".format(event["eventDate"].month)
        + "-"
        + "{:02d}".format(event["eventDate"].day),
        "eventTime": "{:02d}".format(event["eventDate"].hour)
        + ":"
        + "{:02d}".format(event["eventDate"].minute),
        "invitedUsers": event["invitedUsers"],
        "biorhythmType": event["biorhythmType"],
    }
    print(event["eventDate"])
    return event


def postEvent(newEvent):
    eventTime = datetime.datetime.strptime(newEvent["eventTime"], "%H:%M").time()
    eventDate = datetime.datetime.strptime(newEvent["eventDate"], "%Y-%m-%d")
    newEvent["eventDate"] = datetime.datetime.combine(eventDate, eventTime)
    newEventId = eventDAO.postNewEvent(event=newEvent)
    return str(newEventId)


def updateEvent(eventId: ObjectId, newValues):
    eventTime = datetime.datetime.strptime(newValues["eventTime"], "%H:%M").time()
    eventDate = datetime.datetime.strptime(newValues["eventDate"], "%Y-%m-%d")
    newValues["eventDate"] = datetime.datetime.combine(eventDate, eventTime)
    eventUpdate = eventDAO.updateEvent(eventId, newValues)
    return eventUpdate


def uninviteFriendFromEvent(eventId: ObjectId, uninvited: str):
    event = getEvent(eventId)
    uninvited = userDAO.getUserById(userId=ObjectId(uninvited))
    invitedList = event["invitedUsers"]
    invitedList.remove(
        {"userId": str(uninvited["_id"]), "username": uninvited["username"]}
    )
    eventDAO.un_inviteFriend(eventId, invitedList)
    return 0


def inviteFriendToEvent(eventId: ObjectId, invited: str):
    event = getEvent(eventId)
    userToInvite = userDAO.getUserById(userId=ObjectId(invited))
    invitedList = event["invitedUsers"]
    invitedList.append(
        {"userId": str(userToInvite["_id"]), "username": userToInvite["username"]}
    )
    eventDAO.un_inviteFriend(eventId, invitedList)
    return 0


def inviteAllFriends(eventId: ObjectId, allList):
    event = getEvent(eventId)
    invitedList = event["invitedUsers"]
    for invited in allList:
        invitedList.append(invited)
    eventDAO.un_inviteFriend(eventId, invitedList)
    return 0


def deleteEvent(eventId: ObjectId):
    eventDAO.deleteEvent(eventId)
    return 0


def getUsers() -> List[dict]:
    users = userDAO.getAllUsers()
    return users
