from biorhythm import app
from flask import render_template, redirect, request
import jwt

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        # login
        pass
    return render_template("login.html")