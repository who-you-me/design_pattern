# coding: utf-8

import sys

from bigstring import BigString

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python flyweight.py digits")
        print("Example: python flyweight.py 1212123")
        sys.exit()

    bs = BigString(sys.argv[1])
    bs.print()
