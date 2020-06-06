#!/bin/python3

import math
import os
import random
import re
import sys


# New Year Chaos
def inputMinimumBribes():
    # input minimumBribes
    t = 2
    n = 8
    q = "5 1 2 3 7 8 6 4"
    q = list(map(int, q.rstrip().split()))
    minimumBribes(q)
    n = 8
    q = "1 2 5 3 7 8 6 4"
    q = list(map(int, q.rstrip().split()))
    minimumBribes(q)


def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if i < q[i] - 3:
            print("Too chaotic")
            return
        for x in q[max(0, q[i] - 2): i]:
            if x > q[i]:
                bribes += 1
    print(bribes)
