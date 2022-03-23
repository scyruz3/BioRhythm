from datetime import datetime, time
from biorhythm.manager import biorhythmManager
from biorhythm.utils import SignUpForm
from biorhythm.dao import userDAO
from bson.binary import Binary

def registerUser(form: SignUpForm):
    # create an encoded version of the profile image
    encodedPfp = Binary(form.photo.data.read())
    
    # convert date to datetime for compatibility
    convertedDate = datetime.combine(form.birthdate.data, time())

    # create new user based on user model
    newUser = {
        "username": form.username.data, 
        "email": form.email.data,
        "password": form.password.data,
        "birthdate": convertedDate,
        "photo": encodedPfp,
        "biorhythm": biorhythmManager.calculateBioRhythm(convertedDate)
    }
    #TODO: check if the user already exists
    userDAO.insertUser(newUser)
    return