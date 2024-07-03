#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re

def read_input(input):
    for line in input:
        # Use regex to convert text to alphanumeric and remove extra spaces
        # Convert text to lowercase
        # split the line into words; keep returning each word
        line = re.sub("[^0-9a-z]", " ", line.strip().lower())
        line = re.sub("  +", " ", line)
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        # If length of words less than 2 there would be not bigrams
        if len(words) < 2:
            continue
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        
        # Assuming each line is a separate document
        for i in range(len(words)):
            if i == len(words) - 1:
                # Last word in the line, no word follows
                continue
            if words[i] == "bad":
                # Emit the bigram "bad <next_word>" with count 1
                print('%s %s%s%d' % (words[i], words[i+1], separator, 1))

# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()

