#!/usr/bin/env python
#
# rand_MAC.py

import random, argparse, sys

# Function Defs
def rand_MAC():
    # create random int value from 00-ff, format using Hex format spec
    # loop 6 times and accumulate each iteration into an array
    # join array elements into a string by a ":" character, and return array as string
    a = ":".join([format(random.randrange(0x00,0xff), '02x') for i in range(6)])
    return a

# CLI arguments
ex = '''example:
python rand_MAC.py
python rand_MAC.py -n 10'''
parser = argparse.ArgumentParser(prog='rand_MAC', 
                                description='Returns a random MAC address.',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
parser.add_argument("-m", "--MAC", help="<optional>", dest='func', action="store_const", const=rand_MAC)
parser.add_argument("-n", "--number", type=int, help="output multiple MACs", default=1)
parser.set_defaults(func=rand_MAC)
args = parser.parse_args()

def main():
    for i in range(args.number):
          print(args.func())

if __name__ == "__main__":
    sys.exit( main() )
