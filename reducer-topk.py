#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

from operator import itemgetter
import sys
import heapq

def read_mapper_output(input, separator='\t'):
    for line in input:
        yield line.rstrip().split(separator, 1)

def main(separator='\t', k=10):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # Use a priority queue to keep track of the top k words based on their counts
    top_k_words = []
    current_word = None
    current_count = 0
    # Iterate through data
    for word, count_str in data:
        try:
            count = int(count_str)
            # Increase count if word co-occurance reoccurs
            if current_word == word:
                current_count += count
            else:
                # Process the previous word
                if current_word is not None:
                    heapq.heappush(top_k_words, (current_count, current_word))
                    # If the size of the priority queue exceeds k, pop the smallest element
                    if len(top_k_words) > k:
                        heapq.heappop(top_k_words)
                # Start counting for the new word
                current_word = word
                current_count = count
        except ValueError:
            # count was not a number, so silently discard this item
            pass
    # Process the last word
    if current_word is not None:
        heapq.heappush(top_k_words, (current_count, current_word))
        # If the size of the priority queue exceeds k, pop the smallest element
        if len(top_k_words) > k:
            heapq.heappop(top_k_words)
    # Print the top k words in descending order of count
    while top_k_words:
        total_count, current_word = heapq.heappop(top_k_words)
        print("%s%s%d" % (current_word, separator, total_count))

if __name__ == "__main__":
    main()

