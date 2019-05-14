import requests
import json

def proceed_to_cobranca(valor_emprestimo, emprestimo_id):

  payload = {'valor_cobranca': valor_emprestimo, 'emprestimo_id': emprestimo_id}

  req = requests.post(
    'http://0.0.0.0:5002/cobrancas',
    data=json.dumps(payload), headers={'Content-type': 'application/json'}
  )

  return req.json()