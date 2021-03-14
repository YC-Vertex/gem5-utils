import os
import re
import argparse

class BaseUtil():

    base_dir = os.path.expanduser('~/gem5')
    log_dir = os.path.join(base_dir, 'log')

    isa = 'power64'
    isa_dir = os.path.join(base_dir, 'src/arch/' + isa + '/isa')

    def __init__(self):
        pass

def match(path, regex):
    files = []
    result = []

    if os.path.isfile(path):
        files = [path]
    
    elif os.path.isdir(path):
        for root, dirs, fs in os.walk(path):
            for f in fs:
                if os.path.splitext(f)[1] == '.log':
                    files.append(os.path.join(root, f)) 

    for f in files:
        with open(f, 'r') as f:
            for line in f.readlines():
                result += regex.findall(line)
        
    return result

parser = argparse.ArgumentParser(description='Utilities for Gem5')

