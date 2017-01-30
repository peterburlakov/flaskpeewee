from app import db
from peewee import *


class Person(db.Model):
    email = CharField()
    first_name = CharField()
    last_name = CharField()
