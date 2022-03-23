from biorhythm.models import userModel
from biorhythm.utils import SignUpForm


def registerUser(form: SignUpForm):
    # create new user based on user model
    newUser = userModel.User(
        username=form.username.data, 
        birthdate=form.birthdate.data, 
        email=form.email.data, 
        password=form.password.data)
    return 0