from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db.config import configuration
from flask_cors import CORS
from flask_migrate import Migrate
import os
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
database_setup = configuration(app)
db = SQLAlchemy(database_setup)
migrate = Migrate(app=app, db=db)
marshmallow = Marshmallow(app)


# @app.before_first_request
def create_tables():
  db.create_all()


import models
from resources import IndexResource, EmprestimoResource

api.add_resource(IndexResource.IndexResource, '/emprestimo/index')
api.add_resource(EmprestimoResource.EmprestimoResource.get, '/emprestimo')
api.add_resource(EmprestimoResource.EmprestimoResource.get, '/emprestimo/<int:id>')
api.add_resource(EmprestimoResource.EmprestimoResource.post, '/emprestimo')
api.add_resource(EmprestimoResource.EmprestimoResource.put, '/emprestimo/<int:id>')
api.add_resource(EmprestimoResource.EmprestimoResource.delete, '/emprestimo/<int:id>')