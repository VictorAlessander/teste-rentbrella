from flask_restful import Resource
from rq.job import Job
from main import conn


class CobrancaJobResource(Resource):

  def get(self, job_key):
    job = Job.fetch(job_key, connection=redis_connection)

    return str(job.result()), 200