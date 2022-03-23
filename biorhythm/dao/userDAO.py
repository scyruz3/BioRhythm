from biorhythm import mongo
from bson import ObjectId
from biorhythm.models import userMODEL

User = userMODEL()
db = mongo.db


def create_user(user):
    user = User()
    return f'{user.username} : {user.email} : {user.date_created} '

def get_user_by_id(userId: ObjectId):
    user = db.UserData.find_one({"_id": userId})
    return user


def get_user_biorhythm(userId: ObjectId):
    user = db.UserData.find_one({"_id": userId})
    return user["biorhythm"]


def update_user_biorhythm(userId: ObjectId, biorhythm: dict):
    db.UserData.update_one(
        {"_id": userId}, {"$set": {"biorhythm": biorhythm}}
    ).modified_count
    user = db.UserData.find_one({"_id": userId})
    return user
