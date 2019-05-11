from main import db


class Emprestimo(db.Model):

  __tablename__ = 'emprestimos'

  id = db.Column(db.Integer, primary_key=True)
  nome_emprestimo = db.Column(db.String(100), nullable=False, unique=False)
  cobrancas = db.relationship('Cobranca', backref='emprestimo', lazy=True)

  def save(self):
    db.session.add(self)
    db.session.commit()