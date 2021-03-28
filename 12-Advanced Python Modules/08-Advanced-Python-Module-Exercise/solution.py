# -*- coding: utf-8 -*-
"""
Section 12 Puzzle Solution
"""
import zipfile
import os
import re

zipped_file = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
zipped_file.extractall('extracted_content')

with open('extracted_content/extracted_content/Instructions.txt') as f:
    contents = f.read()
    print(contents)
    f.close()

for root, directory, files in os.walk('extracted_content/extracted_content'):
    for file in files:
        file = open(root+"/"+file)     
        contents = file.read()
        match = re.search("\d{3}-\d{3}-\d{4}", contents)
        if match:
            print("SOLUTION: ", match.group())
        file.close()
