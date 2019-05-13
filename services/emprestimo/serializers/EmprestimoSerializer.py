from main import marshmallow


class EmprestimoSerializer(marshmallow.Schema):
  class Meta:
    fields = ('id', 'nome_emprestimo', 'status')


emprestimo_serialized = EmprestimoSerializer()