from datetime import datetime
from enum import unique
from mongoengine import Document, StringField, ImageField,  DateField, EmailField, BinaryField, DateTimeField

class User(Document):
    username = StringField(unique = True, required = True)
    email = EmailField (unique = True)
    birthdate = DateField()
    password = BinaryField(required = True)
    img = ImageField()
    date_created = DateTimeField(default=datetime.utcnow)



    def __init__(self, id, username, birthdate, email, img, password, date_created):
        self.id = id
        self.username = username
        self.birthdate = birthdate
        self.email = email
        self.img = img
        self.password = password
        self.date_created = date_created
        self.is_admin = False

    def get_id (self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_birthdate(self):
        return self.birthdate

    def set_birthdate(self, birhdate):
        self.birthdate = birhdate

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_img(self):
        return self.image_file

    def set_img(self, img):
        self.image_file = img

    def get_password(self) :
        return self.password

    def get_admin(self):
        return self.is_admin

    def set_admin(self):
        self.is_admin = True   