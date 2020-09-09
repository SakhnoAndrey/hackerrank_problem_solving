#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant():
    # input sockMerchant(n, ar)
    n = int(9)
    s = "10 20 20 10 10 30 50 10 20"
    ar = list(map(int, s.rstrip().split()))

    # function sockMerchant(n, ar)
    d = {ar[0]: 0}
    for i in range(0, n):
        if ar[i] in d:
            d[ar[i]] += 1
        else:
            d[ar[i]] = 1
    number_pair = 0
    for k in d:
        number_pair += d[k] // 2
    return number_pair


def countingValleys():
    # input countingValleys(n, s)
    n = 8
    s = "UDDDUDUU"

    # function countingValleys
    down_up = {"D": -1, "U": 1}
    h = 0
    v = 0
    for symb in s:
        if h == 0 and symb == "D":
            v += 1
        # h = h + 1 if symb == 'U' else h - 1
        h += down_up[symb]
    return v


def repeatedString():
    # input repeatedString(s, n):
    s = "a"
    n = 1000000000000

    # function repeatedString
    k_full_string = n // len(s)
    k_el_end_str = n % len(s)
    count_a = k_full_string * s.count("a") + s[:k_el_end_str].count("a")
    return count_a


def jumpingOnClouds():
    # input jumpingOnClouds
    n = int(6)
    s = "0 0 0 0 1 0"
    c = list(map(int, s.rstrip().split()))

    # fucntion jumpingOnClouds
    n = len(c)
    position = 0
    min_num = 0
    while position < n - 1:
        if position + 2 < n:
            position = position + 2 if c[position + 2] == 0 else position + 1
        else:
            position += 1
        min_num += 1
    return min_num


# Grading Students
def grading_studets():
    # Input
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    # Function
    result = [i if (i < 38) or (i % 5 < 3) else (i + 5 - i % 5) for i in grades]
    print(result, sep="\n")


# Apple and Orange
def apple_orange():
    # Input
    s, t = map(int, input().strip().split())
    a, b = map(int, input().strip().split())
    m, n = map(int, input().strip().split())
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    # Function
    count_apple = sum(s <= a + el <= t for el in apples)
    count_orange = sum(s <= b + el <= t for el in oranges)
    print(count_apple, count_orange, sep="\n")


# Kangaroo
def kangaroo():
    # Input
    x1, v1, x2, v2 = map(int, input().strip().split())

    # Function
    if x1 == x2 and v1 == v2:
        result = "YES"
    elif x1 == x2 or v1 == v2:
        result = "NO"
    elif (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        result = "YES"
    else:
        result = "NO"


# Between Two Sets
def between_two_sets():
    # Input
    n, m = map(int, input().strip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    # Function
    max_a = max(a)
    min_b = min(b)
    count = 0
    for elem in range(max_a, min_b + 1):
        res_a = all(elem % el == 0 for el in a)
        res_b = all(el % elem == 0 for el in b)
        print(res_a, res_b)
        count += res_a * res_b
    print(count)


# Breaking the Records
def breaking_records():
    # Input
    n = int(input())
    scores = list(map(int, input().rstrip().split()))

    # Function
    min_score = max_score = scores[0]
    times = [0, 0]
    for elem in scores:
        if elem < min_score:
            min_score = elem
            times[1] += 1
        if elem > max_score:
            max_score = elem
            times[0] += 1
    print(" ".join(map(str, times)))


# Birthday Chocolate
def birthday_chocolate():
    # Input
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    d, m = map(int, input().rstrip().split())

    # Function
    quantity = sum([sum(s[i : i + m]) == d for i in range(n - m + 1)])
    print(quantity)


# Divisible Sum Pairs
def divisible_sum_pairs():
    # Input
    n, k = map(int, input().rstrip().split())
    ar = list(map(int, input().rstrip().split()))

    # Function
    quantity = sum(
        sum((ar[i] + el) % k == 0 for el in ar[i + 1 :]) for i in range(n - 1)
    )
    print(quantity)
    # quantity += sum((ar[i] + el) % k == 0 for el in ar[i+1:])


divisible_sum_pairs()
