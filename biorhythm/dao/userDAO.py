import datetime
from biorhythm import mongo
from bson import ObjectId

db = mongo.db


def getUserById(userId: ObjectId):
    user = db.UserData.find_one({"_id": userId})
    return user


def findUsersByUsername(username: str):
    query = {"username": {
        "$regex": f'.*{username}.*',
        "$options": 'i'
    }}
    results = db.UserData.find(query)
    return results


def getUserBioRhythm(userId: ObjectId):
    user = db.UserData.find_one({"_id": userId})
    return user["biorhythm"]


def updateUserBioRhythm(userId: ObjectId, biorhythm: dict):
    db.UserData.update_one(
        {"_id": userId}, {"$set": {"biorhythm": biorhythm}}
    ).modified_count
    user = db.UserData.find_one({"_id": userId})
    return user


def insertUser(username: str, birthdate: datetime.datetime, biorythm: dict):
    birthdate_mongo: birthdate.replace(microsecond=0)
    new_user = {"username": username,
                "biorhythm": biorythm, "birthdate": birthdate}
    inserted_user = db.UserData.insert_one(new_user)

    return inserted_user.inserted_id
