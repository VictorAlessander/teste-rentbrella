from flask_restful import reqparse, Resource
from constants import ErrorsConstants
from serializers import CobrancaSerializer
from models.Cobranca import Cobranca
from main import redis_queue
from update_emprestimo_status import update_emprestimo_status


class CobrancaResource(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()

  def get(self, id=None):
    if id and id != '':
      cobranca = Cobranca.find_cobranca_by_id(id)
      if cobranca:
        return CobrancaSerializer.cobranca_serialized.jsonify(cobranca)
      else:
        return {'message': 'Cobranca nao encontrada'}, 404
    else:
      return Cobranca.get_all_cobrancas()

  def post(self, id=None):
    self.parser.add_argument(
      'valor_cobranca', required=True, location="json",
      help="Favor inserir um valor para a cobranca"
    )

    self.parser.add_argument(
      'emprestimo_id', required=True, location="json",
      help="Favor inserir o id do emprestimo referenciado a cobranca"
    )

    data = self.parser.parse_args()

    nova_cobranca = Cobranca(
      valor_cobranca=data['valor_cobranca'],
      emprestimo_id=data['emprestimo_id']
    )

    try:
      nova_cobranca.save()

      # job = redis_queue.enqueue_call(
      #   func=update_emprestimo_status,
      #   kwargs=dict(emprestimo_id=data['emprestimo_id'], status=True),
      #   result_ttl=200
      # )

      # return {'message': 'Cobranca salva com sucesso. Job id gerado: {}'.format(job.get_id())}, 200
      return {'message': 'Cobranca salva com sucesso.'}, 200
    except Exception as err:
      print(err)
      return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500

  def put(self, id):
    if id is None:
      return {'message': 'Insira o id da cobranca.'}
    else:
      self.parser.add_argument(
        'valor_cobranca', required=False, location="json",
        help="Favor inserir um valor para a cobranca"
      )

      self.parser.add_argument(
        'emprestimo_id', required=False, location="json",
        help="Favor inserir o id do emprestimo referenciado a cobranca"
      )

      data = self.parser.parse_args()

      cobranca_existente = Cobranca.find_cobranca_by_id(id)

      if cobranca_existente:
        cobranca_existente.valor_cobranca = valor_cobranca=data['valor_cobranca']
        cobranca_existente.emprestimo_id = emprestimo_id=data['emprestimo_id']

        try:
          cobranca_existente.save()
          return {'message': 'Cobranca alterada com sucesso.'}, 200
        except Exception as err:
          print(err)
          return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
      else:
        return {'message': 'Cobranca nao encontrada.'}, 404

  def delete(self, id):
    if id is None:
      return {'message': 'Insira o id da cobranca.'}
    else:
      try:
        if Cobranca.remove(id):
          return {'message': 'Cobranca removida com sucesso'}, 200
        else:
          return {'message': 'Cobranca nao encontrada.'}, 404
      except Exception as err:
        print(err)
        return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500