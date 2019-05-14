import requests
import json


def update_emprestimo_status(emprestimo_id, status):

  payload = {'status': status, 'emprestimo_id': emprestimo_id}

  req = requests.put(
    'http://0.0.0.0:5001/emprestimos/{:d}'.format(emprestimo_id),
    data=json.dumps(payload), headers={'Content-type': 'application/json'}
  )

  return req.json()