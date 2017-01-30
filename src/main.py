# from auth import *
from api import api
# from views import *
from app import app, db

api.setup()


def create_tables():
    print('Safe tables creation')
    from models import Person
    db.database.create_tables([Person], safe=True)


create_tables()

if __name__ == '__main__':
    app.run()
