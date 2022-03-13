from typing import List
from biorhythm import mongo
from bson import ObjectId, json_util
import json

db = mongo.db


def getEventsCreatedByUser(userId: ObjectId) -> List[dict]:
    query = {"creator": str(userId)}
    # process cursor data type
    createdEvents = json.loads(json_util.dumps(db.Events.find(query)))
    return createdEvents
