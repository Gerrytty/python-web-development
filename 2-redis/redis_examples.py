import redis

# Connect to regis
r = redis.Redis(host='localhost', port=6379, db=0)

r.set('name', 'Julia')
print("key 'name' exists?", r.exists('name')) # -> 1
print(r.get('name'))

# set key with expiration timer
r.setex(name='expired_key', time=60, value='data')

# delete key
r.delete('name')
print("key 'name' exists?", r.exists('name'))

# set ttl for key
r.expire('name', 30)

r.set('counter', 0)
# increment value
r.incr('counter')
print(r.get('counter')) # -> 1
