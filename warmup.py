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


# Compare the Triplets
def compare_triplets():
    # Input
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    # Function
    score = [0, 0]
    for x, y in zip(a, b):
        score[0] += x > y
        score[1] += x < y
    print(" ".join(map(str, score)))


compare_triplets()
