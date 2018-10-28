#!bin/env/python
'''mapper.py'''

import sys

# input comes from STDIN ( standard input )
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # strip the line into words
    node, adjNodes = line.split(':')
    adjNodes = adjNodes.split(' ')
    for adjNode1 in adjNodes:
        print(str((node,adjNode1))+'\t'+str(-1))      # use flag -1 to denote the direct adjcent
        for adjNode2 in adjNodes:
            if adjNode1 != adjNode2:
                print(str((adjNode1,adjNode2))+'\t'+node)




