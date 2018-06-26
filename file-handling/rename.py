import os

""" 
Renames the filenames within the same directory as specified below:
	Changes spaces to hyphens

Usage:
python rename.py
"""

path =  os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
    os.rename(filename, filename.replace(" ", "-"))