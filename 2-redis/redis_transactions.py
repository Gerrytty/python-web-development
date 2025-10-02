import redis

r = redis.Redis(host='localhost', port=6379, db=0)
pipe = r.pipeline()
pipe.set('x', 1)
pipe.incr('x')
pipe.execute()

pipe = r.pipeline(transaction=True)
pipe.multi()
pipe.set('x', 1)
pipe.incr('x')
pipe.execute()
