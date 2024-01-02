#!/usr/bin/python3
t = 32
for i in range(90, 64, -1):
    print(chr(i+t), end="")
    t = 32 if t == 0 else 0
