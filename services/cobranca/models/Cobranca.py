from main import db


class Cobranca(db.Model):

  __tablename__ = 'cobrancas'

  id = db.Column(db.Integer, primary_key=True)
  nome_cobranca = db.Column(db.String(100), nullable=False, unique=False)
  emprestimo_id = db.Column(db.Integer, db.ForeignKey('emprestimos.id'), nullable=False)

  def save(self):
    db.session.add(self)
    db.session.commit()