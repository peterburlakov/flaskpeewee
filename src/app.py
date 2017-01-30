from flask import Flask
from flask_cache import Cache

# flask-peewee bindings
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('config.Configuration')

cache_config = {'CACHE_TYPE': 'redis',
                'CACHE_REDIS_HOST': 'redis'}
cache = Cache(app, config=cache_config)
cache.init_app(app)

db = Database(app)
