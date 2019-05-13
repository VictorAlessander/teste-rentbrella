from main import marshmallow


class CobrancaSerializer(marshmallow.Schema):
  class Meta:
    fields = ('id', 'nome_cobranca', 'emprestimo_id')


cobranca_serialized = CobrancaSerializer()