#!/usr/bin/env python
import re

words_dict = {}

with open("./attachment/0004.txt", "r") as rfile:
    allwords = re.sub("[\.\!\/_,$%^*():+\"\'\[\]]", "", "".join(rfile.read()))

for word in allwords.split(" "):
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

for key, val in words_dict.items():
    print(key,val)