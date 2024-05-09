#!/usr/bin/python3
import sys

# Slice sys.argv to exclude the first element (script name)
for arg in sys.argv[1:]:
    print(arg)

