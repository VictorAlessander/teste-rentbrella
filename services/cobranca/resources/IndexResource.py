from flask_restful import reqparse, Resource


class IndexResource(Resource):

  def get(self):
    return {'message': 'Cobranca index'}