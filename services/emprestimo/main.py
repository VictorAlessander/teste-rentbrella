from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db.config import configuration
from flask_cors import CORS
from flask_migrate import Migrate
import os
from flask_marshmallow import Marshmallow
from rq import Queue

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
database_setup = configuration(app)
db = SQLAlchemy(database_setup)
migrate = Migrate(app=app, db=db)
marshmallow = Marshmallow(app)


# Redis connection

conn = 'redis://172.20.0.3:6379'
redis_queue = Queue(connection=conn)


@app.before_first_request
def create_tables():
  db.create_all()

import models
from resources import IndexResource, EmprestimoResource, EmprestimoJobResource

api.add_resource(IndexResource.IndexResource, '/emprestimo/index')
api.add_resource(EmprestimoResource.EmprestimoResource, '/emprestimos', '/emprestimos/<int:id>', endpoint='id')
api.add_resource(EmprestimoJobResource.EmprestimoJobResource, '/emprestimojob/<int:job_key>', endpoint="job_key")