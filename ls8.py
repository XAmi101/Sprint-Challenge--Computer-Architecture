#!/usr/bin/env python3

"""Main."""

import sys
# import os
from cpu import *

# basedir = os.path.abspath(os.getcwd())

# filename = "sctest.ls8"

# filepath = os.path.join(basedir, filename)

# cpu = CPU()

# cpu.load(filepath)
# cpu.run()

cpu = CPU()
# Parse the CLI for submitted program commands
# program_file_test = sys.argv
program = sys.argv[1]
cpu.load(program)
cpu.run() 