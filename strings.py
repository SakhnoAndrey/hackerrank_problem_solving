#!/bin/python3

import math
import os
import random
import re
import sys


def twoStrings():
    # Input strings
    s1 = "hello"
    s2 = "world"

    # function twoStrings
    check = False
    for char in s1:
        if char in s2:
            check = True
            break
    return "YES" if check else "NO"


def sherlockAndAnagrams():
    # Input sherlockAndAnagrams
    s = "ifailuhkqq"

    # Function sherlockAndAnagrams
    dict = {}
    count = 0
    l = len(s)
    for i in range(l):
        for j in range(i, l):
            test = list(s[i: j + 1].strip())
            test.sort()
            sort = "".join(test)
            if sort in dict:
                count += dict[sort]
                dict[sort] += 1
            else:
                dict[sort] = 1
    return count
