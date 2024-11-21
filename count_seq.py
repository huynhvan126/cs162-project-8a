# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/20/2024
# Description: Write a generator function named that doesn't require any arguments and generates a sequence.
def count_seq(seq):
    """Generator function for counting sequences."""
    current_term = "2"
    while True:
        yield current_term
        next_term = ""
        count = 1
        for i in range(1, len(current_term)):
            if current_term[i] == current_term[i-1]:
                count += 1
            else:
                next_term += str(count) + current_term[i - 1]
                count = 1
        next_term += str(count) + current_term[-1]
        current_term = next_term