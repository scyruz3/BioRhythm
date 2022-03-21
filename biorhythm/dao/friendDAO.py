import datetime
from biorhythm import mongo
from bson import ObjectId

db = mongo.db


def create_friend_request(requesterID: str, requesteeID: str):
    created = datetime.datetime.today().replace(microsecond=0)
    new_friend_request = {"requesterID": requesterID,
                          "requesteeID": requesteeID, "created": created, "status": "pending"}
    inserted_request = db.FriendRequests.insert_one(new_friend_request)

    return inserted_request.inserted_id
