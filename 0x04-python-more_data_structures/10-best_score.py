#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest = 0
        key = ""
        for i, y in a_dictionary.items():
            if y > biggest:
                key = i
                biggest = y
        return key
