#!/usr/bin/env python

import random

n = 100

while n > 0:
    print("".join(random.choices("ABCDEFGHJKMNPQRSTUVWXYZ1234567890",k=10)))
    n -= 1