#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    theNum = 0
    last = 0
    rank = {'M':1000, 'X':10, 'C':100, 'I':1, 'V':5, 'L':50, 'D':500}
    for char in reversed(roman_number):
        if (rank[char] >= last):
            theNum += rank[char]
            last = rank[char]
        else:
            theNum -= rank[char]
    return theNum
