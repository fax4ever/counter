#!/usr/bin/env python3

import json

words = {}
max_word = ""
max_count = 0

with open("infinispan.txt", "r") as inputFile:
    for line in inputFile:
        for word in line.split():
            words[word] = words.get(word, 0) + 1
            if (words[word] > max_count):
                max_word = word
                max_count = words[word]

print(words)

with open("words.json", "w") as dump:
        json.dump(words, dump, indent="\t")

print("max word: '{}' - max count: {}".format(max_word, max_count))          