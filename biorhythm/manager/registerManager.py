from datetime import datetime, time
from xml.dom import UserDataHandler
from biorhythm.manager import biorhythmManager
from biorhythm.utils import SignUpForm
from biorhythm.dao import userDAO
from bson.binary import Binary
import bcrypt


def registerUser(form: SignUpForm):
    # create an encoded version of the profile image
    encodedPfp = Binary(form.photo.data.read())

    # convert date to datetime for compatibility
    convertedDate = datetime.combine(form.birthdate.data, time())

    # hash the password
    hashedPass = bcrypt.hashpw(bytes(form.password.data, "utf-8"), bcrypt.gensalt())
    # create new user based on user model
    newUser = {
        "username": form.username.data,
        "email": form.email.data,
        "password": hashedPass,
        "birthdate": convertedDate,
        "photo": encodedPfp,
        "biorhythm": biorhythmManager.calculateBioRhythm(convertedDate),
    }

    # check if the user already exists
    exists = userDAO.findSingleUserByUsername(form.username.data)
    if exists:
        return "User already exists"

    userDAO.insertUser(newUser)
    return
