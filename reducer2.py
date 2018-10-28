#!bin/env/python

import sys

totalTrianglesNumber = 0

for line in sys.stdin:
    line = line.strip()
    total, triangleNumber = line.split('\t')
    totalTrianglesNumber += eval(totalTrianglesNumber)

print(totalTrianglesNumber*1.0/6)
