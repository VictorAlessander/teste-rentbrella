from flask_restful import reqparse, Resource
from models.Emprestimo import Emprestimo
from serializers import EmprestimoSerializer
from constants import ErrorsConstants
from main import redis_queue
from proceed_to_cobranca import proceed_to_cobranca


class EmprestimoResource(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()


  def get(self, id=None):
    if id and id != '':
      emprestimo = Emprestimo.find_emprestimo_by_id(id)
      if emprestimo:
        return EmprestimoSerializer.emprestimo_serialized.jsonify(emprestimo)
      else:
        return {'message': 'Emprestimo nao encontrado'}
    else:
      return Emprestimo.get_all_emprestimos()
  
  def post(self, id=None):
    self.parser.add_argument(
      'nome_emprestimo', required=True, location="json",
      help="Favor inserir um nome para o emprestimo"
    )

    self.parser.add_argument(
      'valor_emprestimo', required=True, location="json",
      help="Favor inserir um valor para o emprestimo"
    )

    data = self.parser.parse_args()

    novo_emprestimo = Emprestimo(
      nome_emprestimo=data['nome_emprestimo'],
      valor_emprestimo=data['valor_emprestimo']
    )

    try:
      emprestimo_id = novo_emprestimo.save(novo_emprestimo)

      # cobranca_body = {
      #   'valor_cobranca': data['valor_emprestimo'],
      #   'emprestimo_id': emprestimo_id
      # }

      # redis_connection.hmset('test', cobranca_body)

      # job = redis_queue.enqueue(proceed_to_cobranca, kwargs=cobranca_body)

      job = redis_queue.enqueue_call(
        func=proceed_to_cobranca,
        kwargs=dict(valor_emprestimo=data['valor_emprestimo'], emprestimo_id=emprestimo_id),
        result_ttl=200
      )

      return {'message': 'Emprestimo criado com sucesso. Job id gerado: {}'.format(job.get_id())}, 200
    except Exception as err:
      # print(err)
      raise err
      # return {'message': err}, 500

  def put(self, id):
    if id:
      self.parser.add_argument(
        'nome_emprestimo', required=False, location="json"
      )

      self.parser.add_argument(
        'valor_emprestimo', required=False, location="json"
      )

      data = self.parser.parse_args()

      emprestimo_existente = Emprestimo.find_emprestimo_by_id(id)

      if emprestimo_existente:

        # Valida alteracao nos campos

        if data['nome_emprestimo'] and emprestimo_existente.nome_emprestimo != data['nome_emprestimo']:
          emprestimo_existente.nome_emprestimo = data['nome_emprestimo']

        if data['valor_emprestimo'] and emprestimo_existente.valor_emprestimo != data['valor_emprestimo']:
          emprestimo_existente.valor_emprestimo = data['valor_emprestimo']

        # if data['status'] and emprestimo_existente.status != data['status']:
        #   emprestimo_existente.status = data['status']

        try:
          emprestimo_existente.save()
          return {'message': 'Emprestimo alterado com sucesso.'}, 200
        except Exception as err:
          print(err)
          return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
      else:
        return {'message': 'Emprestimo nao encontrada.'}, 404
    else:
      return {'message': 'Favor inserir o id do emprestimo.'}, 400

  def delete(self, id):
    if id:
      try:
        if Emprestimo.remove(id):
          return {'message': 'Emprestimo removido com sucesso.'}, 200
        else:
          return {'message': 'Emprestimo nao encontrado.'}, 404
      except Exception as err:
        print(err)
        return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
    else:
      return {'message': 'Insira o id do emprestimo.'}, 400

  # @staticmethod
  # def proceed_to_cobranca(kwargs):
  #   # cobranca_body = {
  #   #   'valor_cobranca': valor_emprestimo,
  #   #   'emprestimo_id': emprestimo_id
  #   # }

  #   print(kwargs)
  #   # requests.post(
  #   #   '0.0.0.0:5002/cobrancas',
  #   #   data=cobranca_body
  #   # )