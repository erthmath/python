#!/usr/bin/env python3

import os, re

files = os.listdir(os.getcwd())
txt_files = []

txt_regex = re.compile(r'.txt')

for doc in files:
    if txt_regex.search(doc) is not None:
        txt_files.append(doc)

search_regex = re.compile(r'\s?\w*\!')

for doc in txt_files:
    opened_file = open('{0}/{1}'.format(os.getcwd(), doc))
    contents = opened_file.read()
    string = ''.join(contents)
    found = search_regex.findall(string)
    found_str = ''.join(found)
    print(found_str)
