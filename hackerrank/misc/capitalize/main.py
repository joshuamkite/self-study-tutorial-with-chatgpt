#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    elements = re.split(r'(\s+)', s)
    capitalized_elements = [element.capitalize(
    ) if element.strip() else element for element in elements]
    result = ''.join(capitalized_elements)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
