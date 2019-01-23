#!/usr/bin/env python
#
# rand_MAC.py
# A script to output random MAC addresses
# example usage:
# python rand_MAC.py -n 10
# outputs 10 random MAC addresses

import random, argparse

# CLI arguments
parser = argparse.ArgumentParser(description='Returns a random MAC address.')
parser.add_argument("-n", "--number", type=int, help="Number of MAC addresses to output")
args = parser.parse_args()

# Function Defs
def rand_MAC():
    # for loop creating hex mumber using randint(1,0xff)
    # accumulate 6 iterations of hex number in array
    # concat array elements and return
    # THIS DOESN"T WORK YET, PLZ FIX
    arr = [0]
    for i in range(6):
        arr.append(random.randint(1,16)
    return ":".join(str(arr))

# Main logic - Check if no arguments were passed, and output an ipv4 address (default)
# if a value was specified as a flag -n, check if -v6 flag also passed and output -v6 format n times
# if a value was specified as a flag -n, and -v6 flag not set, output -v4 format, n times
# if no value was specified as -n, check if -v4 or -v6 flag were specified and output in that
# respective format
# if no flags specified, output a single v4 address (default) 
def main():
    if not len(sys.argv) > 1:
        print(rand_MAC())
    else args.number:
        for i in range(args.number):
                print(rand_MAC())

if __name__ == "__main__":
    main()
