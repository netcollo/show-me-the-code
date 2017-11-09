#1/usr/bin/env python

import random, redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

n = 1
while n <= 200:
    pcode = "".join(random.choices("ABCDEFGHJKMNPQRSTUVWXY1234567890",k=10))
    r.sadd("promocode", pcode)
    n += 1
r.save()
