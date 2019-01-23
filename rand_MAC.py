#!/usr/bin/env python
#
# rand_MAC.py

import random, argparse

# Function Def
def rand_MAC():
    # for loop creating hex mumber list using randint(1,0xff)
    # accumulate 6 iterations of hex number in array
    # concat array elements and return
    # THIS DOESN"T WORK YET, PLZ FIX
    # possibly a = map(hex, xrange(6))
    arr = []
    for i in range(6):
        arr.append(random.randint(1,255)
    #debugging
    print(arr)
    print(":".join(str(arr))
    return 

# CLI arguments
ex = '''example:
python rand_MAC.py
python rand_MAC.py -n 10'''
parser = argparse.ArgumentParser(prog='rand_MAC', 
                                description='Returns a random MAC address.',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
parser.add_argument("-m", "--MAC", dest='func', action="store_const", const=rand_MAC)
parser.add_argument("-n", "--number", type=int, help="output multiple MACs", default=1)
parser.set_defaults(func=rand_MAC)
args = parser.parse_args()

def main():
    for i in range(args.number):
          print(args.func())

if __name__ == "__main__":
    main()
