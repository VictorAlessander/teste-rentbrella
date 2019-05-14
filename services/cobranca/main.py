from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db.config import configuration
from flask_cors import CORS
from flask_migrate import Migrate
import os
from flask_marshmallow import Marshmallow
from rq import Queue
import redis

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
database_setup = configuration(app)
db = SQLAlchemy(database_setup)
migrate = Migrate(app=app, db=db)
marshmallow = Marshmallow(app)

# Redis connection

conn = '172.20.0.3'
redis_connection = redis.Redis(conn)
redis_queue = Queue('default', connection=redis_connection)

@app.before_first_request
def create_tables():
  db.create_all()

import models
from resources import IndexResource, CobrancaResource, CobrancaJobResource

api.add_resource(IndexResource.IndexResource, '/cobranca/index')
api.add_resource(CobrancaResource.CobrancaResource, '/cobrancas', '/cobrancas/<int:id>', endpoint='id')
api.add_resource(CobrancaJobResource.CobrancaJobResource, '/cobranca/<int:job_key>', endpoint="job_key")