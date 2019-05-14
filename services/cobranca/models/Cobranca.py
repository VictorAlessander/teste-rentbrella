from main import db


class Cobranca(db.Model):

  __tablename__ = 'cobrancas'

  id = db.Column(db.Integer, primary_key=True)
  valor_cobranca = db.Column(db.String(100), nullable=False, unique=False)
  emprestimo_id = db.Column(db.Integer, unique=False, nullable=False)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_cobranca_by_id(cls, id):
    return Cobranca.query.filter_by(id=id).first()

  @classmethod
  def remove(cls, id):
    cobranca = Cobranca.find_cobranca_by_id(id)

    if cobranca:
      db.session.delete(cobranca)
      db.session.commit()
      return True
    else:
      return False

  @classmethod
  def get_all_cobrancas(cls):
    def to_json(x):
      return {
        'id': x.id,
        'valor_cobranca': x.valor_cobranca,
        'emprestimo_id': x.emprestimo_id
      }
    return {'cobrancas': list(map(lambda x: to_json(x), Cobranca.query.all()))}