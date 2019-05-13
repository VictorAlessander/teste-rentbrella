from flask_restful import reqparse, Resource
from constants import ErrorsConstants
from serializers import CobrancaSerializer
from models.Cobranca import Cobranca
import requests
import json
from main import redis_queue


class CobrancaResource(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()

  def get(self, id=None):
    if id is not None:
      cobranca = Cobranca.find_cobranca_by_id(id)
      if cobranca:
        return CobrancaSerializer.cobranca_serialized.jsonify(cobranca)
      else:
        return {'message': 'Cobranca nao encontrada'}, 404
    else:
      return CobrancaSerializer.cobranca_serialized.jsonify(Cobranca.get_all_cobrancas())

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

      status_emprestimo = True
      emprestimo_body = {'status': status_emprestimo}

      job = redis_queue.enqueue_call(
        func=proceed_to_emprestimo,
        args=(data['emprestimo_id'], emprestimo_body,),
        result_ttl=5000
      )

      print(job.get_id())

      # return {'message': 'Cobranca salva com sucesso.'}, 200
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

  @staticmethod
  def proceed_to_emprestimo(emprestimo_id, emprestimo_body):
    requests.put(
      '0.0.0.0:5001/emprestimos/{:d}'.format(emprestimo_id),
      data=json.dumps(emprestimo_body)
    )