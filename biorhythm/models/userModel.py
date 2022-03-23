from datetime import datetime
from enum import unique
from mongoengine import Document, StringField, ImageField,  DateField, EmailField, BinaryField, DateTimeField


# user model based on mongo document
class User(Document):
    username = StringField(unique = True, required = True)
    email = EmailField (unique = True)
    birthdate = DateField()
    password = BinaryField(required = True)
    img = ImageField()
    date_created = DateTimeField(default=datetime.utcnow)