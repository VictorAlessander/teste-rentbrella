
def configuration(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@172.20.0.2:3306/rentbrellatest'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  # app.config['SECRET_KEY'] = 'ef5bcb77da527eb6901dcaf2ad046e3cab938983b71d6d1c'

  return app