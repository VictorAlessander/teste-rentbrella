from flask_restful import reqparse, Resource
from constants import ErrorsConstants
from serializers import CobrancaSerializer
from models.Cobranca import Cobranca


class CobrancaResource(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()

  def get(self, id=None):
    if id:
      cobranca = Cobranca.find_cobranca_by_id(id)
      if cobranca:
        return CobrancaSerializer.cobranca_serialized.jsonify(cobranca)
      else:
        return {'message': 'Cobranca nao encontrada'}, 404
    else:
      return CobrancaSerializer.cobranca_serialized.jsonify(Cobranca.get_all_cobrancas())

  def post(self):
    self.parser.add_argument(
      'nome_cobranca', required=True, location="json",
      help="Favor inserir um nome para a cobranca"
    )

    self.parser.add_argument(
      'emprestimo_id', required=True, location="json",
      help="Favor inserir o id do emprestimo referenciado a cobranca"
    )

    data = self.parser.parse_args()

    nova_cobranca = Cobranca(
      nome_cobranca=data['nome_cobranca'],
      emprestimo_id=data['emprestimo_id']
    )

    try:
      nova_cobranca.save()
      return {'message': 'Cobranca salva com sucesso.'}, 200
    except Exception as err:
      return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
      print(err)

  def put(self, id):
    self.parser.add_argument(
      'nome_cobranca', required=False, location="json",
      help="Favor inserir um nome para a cobranca"
    )

    self.parser.add_argument(
      'emprestimo_id', required=False, location="json",
      help="Favor inserir o id do emprestimo referenciado a cobranca"
    )

    data = self.parser.parse_args()

    cobranca_existente = Cobranca.find_cobranca_by_id(id)

    if cobranca_existente:
      cobranca_existente.nome_cobranca = nome_cobranca=data['nome_cobranca']
      cobranca_existente.emprestimo_id = emprestimo_id=data['emprestimo_id']

      try:
        cobranca_existente.save()
        return {'message': 'Cobranca alterada com sucesso.'}, 200
      except Exception as err:
        return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
        print(err)
    else:
      return {'message': 'Cobranca nao encontrada.'}, 404

  def delete(self, id):
    try:
      if Cobranca.remove(id):
        return {'message': 'Cobranca removida com sucesso'}, 200
      else:
        return {'message': 'Cobranca nao encontrada.'}, 404
    except Exception as err:
      return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
      print(err)