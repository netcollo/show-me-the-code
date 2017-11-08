#!/usr/bin/env python

import random,pymysql



n = 1
while n <= 200:
    #print("%s:  %s" %(n, "".join(random.choices("ABCDEFGHJKMNPQRSTUVWXY1234567890",k=10))))
    print("".join(random.choices("ABCDEFGHJKMNPQRSTUVWXY1234567890",k=10)))
    n += 1