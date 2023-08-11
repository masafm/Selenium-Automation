#!/usr/bin/env python3
import sys
import xorcrypt

key=sys.argv[1]
if len(sys.argv) > 2:
    print(xorcrypt.decrypt(input(), key))
else:
    print(xorcrypt.crypt(input(), key))
