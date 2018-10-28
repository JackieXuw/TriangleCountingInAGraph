#!/bin/env/python

import sys

currentLowerSideNodes = None
currentLowerSideNodesCorrespondingTrianglesNumber = 0
currentLowerSideConnectIndicator = False  # by default the two nodes on the lower side is thought to be unconnecting


for line in sys.stdin:
    line = line.strip()
    lowerSideNodes, upperNode = line.split('\t')
    lowerSideNodes = eval(lowerSideNodes)
    if lowerSideNodes != currentLowerSideNodes:
        # we meet a new LowerSideNodes
        # first print the currentLowerSideNodes
        if currentLowerSideNodes != None and currentLowerSideConnectIndicator:
            print('Total'+'\t'+str(currentLowerSideNodesCorrespondingTrianglesNumber))

        # initialize the current setting
        currentLowerSideNodes = lowerSideNodes
        currentLowerSideNodesCorrespondingTrianglesNumber = 0
        currentLowerSideConnectIndicator = False

    if upperNode == '-1':
        currentLowerSideConnectIndicator = True
        continue
    else:
        # add triangle counting number
        currentLowerSideNodesCorrespondingTrianglesNumber = currentLowerSideNodesCorrespondingTrianglesNumber + 1


if currentLowerSideNodes != None and currentLowerSideConnectIndicator:
    print('Total'+'\t'+str(currentLowerSideNodesCorrespondingTrianglesNumber))


