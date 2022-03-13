from biorhythm import mongo
from bson import ObjectId

db = mongo.db


def getUserById(userId: ObjectId):
    user = db.UserData.find_one({"_id": userId})
    return user


def getUserBioRhythm(userId: ObjectId):
    user = db.UserData.find_one({"_id": userId})
    return user["biorhythm"]


def updateUserBioRhythm(userId: ObjectId, biorhythm: dict):
    db.UserData.update_one(
        {"_id": userId}, {"$set": {"biorhythm": biorhythm}}
    ).modified_count
    user = db.UserData.find_one({"_id": userId})
    return user
