import requests
import json


def remove_cobranca(emprestimo_id):
  req = requests.delete(
    'http://172.20.0.5:5002/cobrancas/{:d}'.format(emprestimo_id),
    headers={'Content-type': 'application/json'}
  )

  return req.json()