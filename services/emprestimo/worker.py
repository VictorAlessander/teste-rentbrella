import os
import redis
from rq import Worker, Queue, Connection

listen = ['default']

# redis_url = 'redis://172.20.0.3:6379'
redis_url = 'redis://0.0.0.0:6379'
conn = redis.from_url(redis_url)

if __name__ == '__main__':
  with Connection(conn):
    worker = Worker(list(map(Queue, listen)))
    worker.work()