#!/bin/python3

import math
import os
import random
import re
import sys


def solveMeFirst(a, b):
    # Hint: Type return a+b below
    return a + b


# Simple Array Sum
def simple_array_sum():
    # Input
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    # Function
    print(sum(ar))


simple_array_sum()
