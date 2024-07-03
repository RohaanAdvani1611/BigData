#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
from itertools import combinations
import re

def read_input(input):
    for line in input:
        # Use Regex to preprocess text to Alphanumeric
        # Convert to lowercase
        # We can convert lines into set to reduce repeated cooccurances
        # split the line into words; keep returning each word
        line = re.sub("[^0-9a-z]", " ", line.strip().lower())
        line = re.sub("  +", " ", line)
        yield list(set(line.split()))

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        # Lines with less than 2 words have no cooccurances
        if len(words)<2:
            continue
        # write the results to STDOUT (standard output);
        # output word pairs with count as 1 using combinations
        for word_pair in combinations(words, 2):
            print('%s%s%d' % (' '.join(word_pair), separator, 1))

# how to test locally in bash/linux: cat <input> | python mapper.py
if __name__ == "__main__":
    main()

