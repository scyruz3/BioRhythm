import email
from typing_extensions import Self
from biorhythm import mongo
from bson import ObjectId
from biorhythm.MODELS import userMODEL as User

db = mongo.db


def createUser(user):
    user = User()
    return f'{user.username} : {user.email} : {user.date_created} '

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
