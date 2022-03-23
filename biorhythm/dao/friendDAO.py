import datetime
import json
from biorhythm import mongo
from bson import ObjectId, json_util, objectid
from biorhythm.dao import userDAO
from flask import session

db = mongo.db


def get_pending_requests_for_user(userId: str):
    print(f"getting requests for {userId}")
    pending_requests = json.loads(json_util.dumps(
        db.FriendRequests.find({"requesteeID": userId, "status": "pending"})))

    return pending_requests


def find_friend_request(requesterID: str, requesteeID: str):
    existing_request = db.FriendRequests.find_one({"$or": [{"requesterID": requesterID, "requesteeID": requesteeID, "status": "pending"}, {
        "requesterID": requesteeID, "requesteeID": requesterID, "status": "pending"}]})

    print(existing_request)
    return existing_request


def create_friend_request(requesterID: str, requesteeID: str):
    if find_friend_request(requesterID, requesteeID) is not None:
        return None

    created = datetime.datetime.today().replace(microsecond=0)
    new_friend_request = {"requesterID": requesterID,
                          "requesteeID": requesteeID, "created": created, "status": "pending", "requesterUsername": session.get("username")}
    inserted_request = db.FriendRequests.insert_one(new_friend_request)

    return inserted_request.inserted_id
