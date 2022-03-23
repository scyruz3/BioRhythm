import json
from biorhythm import mongo
from bson import ObjectId, json_util
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

def getAllUsers():
    allUsers = json.loads(json_util.dumps(db.UserData.find()))
    return allUsers

def insertUser(user: dict):
    inserted_user = db.UserData.insert_one(user)
    return inserted_user.inserted_id
