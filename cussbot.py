#!/usr/bin/python
#
# cussbot.py - CussBot - a random curseword generator, inspired by Better Off Ted
#
# Usage: chat.py -L -P 
#
# -L - Lembasted - the cleaner version of the formula
# -P - Philibusted - the not-so-clean version of the formula

import getopt
import random
import string
import sys

# Set the default values
RNG = random.SystemRandom()

USAGE_TEXT = """usage: chatgfy.py [-L -P]

-L - Lembasted - the cleaner version of the formula
-P - Philibusted - the not-so-clean version of the formula
"""

print("Remember, employees must now use foul language at work.")
print(USAGE_TEXT)
