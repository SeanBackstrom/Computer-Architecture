#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load()
cpu.run()

print(f"hi {10000010:b}")