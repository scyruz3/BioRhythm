from operator import methodcaller
from os import stat
from biorhythm import app
from biorhythm.manager import friendManager
from flask import render_template, request, Response


@app.route("/friend-requests", methods=["POST", "GET"])
def post_friend_invite():
    if request.method == "POST":
        userID = request.json.get("userID")
        friendID = request.json.get("friendID")

        friendManager.send_friend_invite(userID, friendID)
        return Response(status=201)
    return render_template("tables.html")


@app.route("/friend-requests/find", methods=["POST"])
def find_friend_invite():
    userID = request.json.get("userID")
    friendID = request.json.get("friendID")

    friendManager.find_request(userID, friendID)
    return Response(status=200)
