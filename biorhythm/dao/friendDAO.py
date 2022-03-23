import datetime
import re
from biorhythm import mongo
from bson import ObjectId

db = mongo.db


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
                          "requesteeID": requesteeID, "created": created, "status": "pending"}
    inserted_request = db.FriendRequests.insert_one(new_friend_request)

    return inserted_request.inserted_id
