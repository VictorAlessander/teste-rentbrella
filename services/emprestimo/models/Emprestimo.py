from main import db


class Emprestimo(db.Model):

  __tablename__ = 'emprestimos'

  id = db.Column(db.Integer, primary_key=True)
  nome_emprestimo = db.Column(db.String(100), nullable=False, unique=False)
  valor_emprestimo = db.Column(db.Float, nullable=False, unique=False)
  # status = db.Column(db.Boolean, unique=False, default=False)

  def save(self, emprestimo):
    db.session.add(emprestimo)
    db.session.commit()
    db.session.refresh(emprestimo)
    return emprestimo.id

  @classmethod
  def remove(cls, id):
    emprestimo = Emprestimo.find_emprestimo_by_id(id)

    if emprestimo:
      db.session.delete(emprestimo)
      db.session.commit()
      return True
    else:
      return False

  @classmethod
  def find_emprestimo_by_id(cls, id):
    return Emprestimo.query.filter_by(id=id).first()

  @classmethod
  def get_all_emprestimos(cls):
    def to_json(x):
      return {
        'id': x.id,
        'nome_emprestimo': x.nome_emprestimo,
        'valor_emprestimo': x.valor_emprestimo
        # 'status': x.status
      }
    return {'emprestimos': list(map(lambda x: to_json(x), Emprestimo.query.all()))}