from flask_restful import reqparse, Resource
from models.Emprestimo import Emprestimo
from serializers import EmprestimoSerializer
from constants import ErrorsConstants


class EmprestimoResource(Resource):

  def __init__(self):
    self.parser = reqparse.RequestParser()


  def get(self, id=None):
    if id:
      emprestimo = Emprestimo.find_emprestimo_by_id(id)
      if emprestimo:
        return EmprestimoSerializer.emprestimo_serialized.jsonify(emprestimo)
      else:
        return {'message': 'Emprestimo nao encontrado'}
    else:
      return EmprestimoSerializer.emprestimo_serialized.jsonify(Emprestimo.get_all_emprestimos())
  
  def post(self):
    self.parser.add_argument(
      'nome_emprestimo', required=True, location="json",
      help="Favor inserir um nome para o emprestimo"
    )

    data = self.parser.parse_args()

    novo_emprestimo = Emprestimo(
      nome_emprestimo=data['nome_emprestimo']
    )

    try:
      novo_emprestimo.save()
      return {'message': 'Emprestimo criado com sucesso.'}
    except Exception as err:
      return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}
      print(err)

  def put(self, id):
    self.parser.add_argument(
      'nome_emprestimo', required=True, location="json",
      help="Favor inserir um nome para o emprestimo"
    )

    data = self.parser.parse_args()

    if id:
      emprestimo_existente = Emprestimo.find_emprestimo_by_id(id)

      if emprestimo_existente:
        emprestimo_existente.nome_emprestimo = data['nome_emprestimo']
        emprestimo_existente.status = data['status']
        try:
          emprestimo_existente.save()
          return {'message': 'Emprestimo alterado com sucesso.'}, 200
        except Exception as err:
          return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
          print(err)
      else:
        return {'message': 'Emprestimo nao encontrada.'}, 404
    else:
      return {'message': 'Favor inserir o id do emprestimo.'}, 400

  def delete(self, id):
    try:
      if Emprestimo.remove(id):
        return {'message': 'Emprestimo removido com sucesso.'}, 200
      else:
        return {'message': 'Emprestimo nao encontrado.'}, 404
    except Exception as err:
      return {'message': ErrorsConstants.ERRO_CONSULTAR_LOGS}, 500
      print(err)