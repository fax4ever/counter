#!/usr/bin/env python3

words = {}

with open("infinispan.txt", "r") as inputFile:
    for line in inputFile:
        for word in line.split():
            words[word] = words.get(word, 0) + 1

print(words)