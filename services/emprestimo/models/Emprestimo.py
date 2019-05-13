from main import db


class Emprestimo(db.Model):

  __tablename__ = 'emprestimos'

  id = db.Column(db.Integer, primary_key=True)
  nome_emprestimo = db.Column(db.String(100), nullable=False, unique=False)
  valor_emprestimo = db.Column(db.Float, nullable=False, unique=False)
  status = db.Column(db.Boolean, unique=False, default=False)

  def save(self):
    db.session.add(self)
    db.session.commit()
    db.session.refresh(self.id)
    return self.id

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
    return Emprestimo.query.all()