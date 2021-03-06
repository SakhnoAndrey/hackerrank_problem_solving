#!/bin/python3

import math
import os
import random
import re
import sys
import copy
import numpy as np


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


# Migratory birds
def migratory_birds():
    # Input
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    # Function
    result = sorted(reversed(list(set(arr))), key=arr.count)[-1]
    print(result)


# Day of programmer
def day_programmer():
    # Input
    year = int(input())

    # Function
    mon7_days = 215  # amount 7 months' days
    if year == 1918:
        feb_days = 15
    elif year < 1918:  # julian year
        feb_days = 29 if year % 4 == 0 else 28
    else:
        feb_days = (
            29 if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else 28
        )
    day = 256 - mon7_days - feb_days
    result = "{0:02}.09.{1}".format(day, year)
    print(result)


# Bon appetit
def bon_appetit():
    # Input
    n, k = map(int, input().rstrip().split())
    bill = list(map(int, input().rstrip().split()))
    b = int(input().rstrip())

    # Function
    result = (
        "Bon Appetit"
        if (sum(bill) - bill[k]) // 2 == b
        else b - (sum(bill) - bill[k]) // 2
    )
    print(result)


# Drawing book
def drawing_book():
    # Input
    n, p = int(input()), int(input())

    # Function
    result = min(p // 2, n // 2 - p // 2)
    print(result)


# Electronics Shop
def electronics_shop():
    # Input
    b, n, m = map(int, input().rstrip().split())
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    # Function
    result = max([x + y if x + y <= b else -1 for x in keyboards for y in drives])
    print(result)


# Cats and mouse
def cats_mouse():
    # Input
    q = int(input())

    # Function
    for _ in range(q):
        x, y, z = map(int, input().rstrip().split())
        if abs(x - z) == abs(y - z):
            result = "Mouse C"
        elif abs(x - z) < abs(y - z):
            result = "Cat A"
        else:
            result = "Cat B"
        print(result)


# Forming a magic square
# generete the magic square
def gen_square(direction):
    ms = [[0] * 3 for i in range(3)]
    ms[1][1] = 5
    even = [2, 4, 6, 8]
    i = 0
    result = []
    for num in even:
        tmp = copy.deepcopy(ms)
        tmp[0][0] = num
        tmp[2][2] = 10 - tmp[0][0]
        can = even[(i + direction) % len(even)]
        if tmp[2][2] == can:
            can = even[(i + direction * 2) % len(even)]
        tmp[0][2] = can
        tmp[2][0] = 10 - tmp[0][2]
        tmp[0][1] = 15 - tmp[0][0] - tmp[0][2]
        tmp[1][0] = 15 - tmp[0][0] - tmp[2][0]
        tmp[1][2] = 10 - tmp[1][0]
        tmp[2][1] = 10 - tmp[0][1]
        i += 1
        result.append(tmp)
    return result


# Complete the formingMagicSquare function below.
def forming_magic_square(s):
    ms1 = gen_square(1)
    ms2 = gen_square(-1)
    ms = ms1 + ms2
    totals = []
    for m in ms:
        total = 0
        for m_row, s_row in zip(m, s):
            for i, j in zip(m_row, s_row):
                total += abs(i - j)
        totals.append(total)
    return min(totals)


# Picking Numbers
def picking_numbers():
    # Input
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    # Function
    length_picking_numbers = max(
        [len(list(filter(lambda x: x == num or x == num + 1, a))) for num in set(a)]
    )
    print(length_picking_numbers)


# Climbing the Leaderboard
def climbing_leaderboard():
    # Input
    n = int(input())
    ranked = list(map(int, input().rstrip().split()))
    m = int(input())
    player = list(map(int, input().rstrip().split()))

    # Function
    scores_set = list(set(ranked))
    scores_set.sort(reverse=True)
    result = []
    l = len(scores_set)
    for s in player:
        while (l > 0) and (s >= scores_set[l - 1]):
            l -= 1
        result.append(l + 1)
    print("\n".join(map(str, result)))


# The hurdle race
def hurdle_race():
    # Input
    n, k = map(int, input().rstrip().split())
    height = list(map(int, input().rstrip().split()))

    # Function
    result = max(height) - k if max(height) - k > 0 else 0
    print(result)


# Designer pdf viewer
def designer_pdf_viewer():
    # Input
    h = list(map(int, input().rstrip().split()))
    word = str(input().rstrip())

    # Function
    result = max(list(map(lambda x: h[ord(x) - 97], word))) * len(word)
    print(result)


# Utopian tree
def utopian_tree():
    # Input
    t = int(input())

    for _ in range(t):
        n = int(input())
        # Function
        h = 1
        for i in range(n):
            h = (h * 2) if i % 2 == 0 else h + 1
        result = h
        # End function
        print(result)


# Angry professor
def angry_professor():
    # Input
    t = int(input())
    for t_itr in range(t):
        n, k = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        # Function
        result = "YES" if n - sum(el > 0 for el in a) < k else "NO"
        # End function
        print(result)


# Beautiful days at the movies
def beautiful_days_movies():
    # Input
    i, j, k = map(int, input().rstrip().split())

    # Function
    result = sum(
        list(map(lambda x: abs(x - int(str(x)[::-1])) % k == 0, range(i, j + 1, 1)))
    )
    print(result)


# Viral advertising
def viral_advertising():
    # Input
    n = int(input())

    # Function
    m = [2]
    for i in range(n - 1):
        m.append(int(3 * m[i] / 2))
    print(m)


# Save the prisoner
def save_prisoner():
    # Input
    t = int(input())
    for _ in range(t):
        n, m, s = map(int, input().rstrip().split())
        # Function
        result = (s - 1 + m - 1) % n + 1
        print(result)


# Circular array rotation
def circular_array_rotation():
    # Input
    n, k, q = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    queries = [int(input()) for _ in range(q)]

    # Function
    result = [a[i - k % n] for i in queries]
    print("\n".join(map(str, result)))


# Sequence equation
def sequence_equation():
    # Input
    n = int(input())
    p = list(map(int, input().rstrip().split()))

    # Function
    result = []
    for i in range(n):
        result.append(p.index(p.index(i + 1) + 1) + 1)
    print("\n".join(map(str, result)))


# Jumping on the clouds: revisited
def jumping_clouds_revisited():
    # Input
    n, k = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))

    # Function
    e = 100
    i = k % n
    e -= 1 + c[i] * 2
    while i != 0:
        i = (i + k) % n
        e -= 1 + c[i] * 2
    print(e)


# Find digits
def find_digits():
    # Input
    t = int(input())
    for _ in range(t):
        n = int(input())
        # Function
        result = sum(a != "0" and n % int(a) == 0 for a in str(n))
        print(result)
        # End function


# Extra long factorials
def extra_long_factorials():
    # Input
    n = int(input())

    # Function
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)


# Append and delete
def append_delete():
    # Input
    s = input()
    t = input()
    k = int(input())

    # Function
    len_s = len(s)
    len_t = len(t)
    num_same_char = 0
    for x, y in zip(s, t):
        if x == y:
            num_same_char += 1
        else:
            break
    extra_s = len_s - num_same_char
    extra_t = len_t - num_same_char
    diff = extra_s + extra_t
    if len_s + len_t < k:
        result = "Yes"
    elif extra_s + extra_t <= k and (extra_s + extra_t - k) % 2 == 0:
        result = "Yes"
    else:
        result = "No"
    print(result)


# Sherlock and Squares
def sherlock_squares():
    # Input
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().rstrip().split())
        a = math.ceil(a ** 0.5)
        b = math.floor(b ** 0.5)
        result = b - a + 1
        print(result)


# Library Fine
def library_fine():
    # Input
    d1, m1, y1 = map(int, input().rstrip().split())
    d2, m2, y2 = map(int, input().rstrip().split())

    # Function
    if y1 > y2:
        result = 10000
    elif y1 == y2 and m1 > m2:
        result = 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        result = 15 * (d1 - d2)
    else:
        result = 0
    print(result)


# Cut the sticks
def cut_sticks():
    # Input
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    # Function
    result = []
    for x in sorted(set(arr)):
        result.append(n)
        n -= arr.count(x)
    print(result)


# Non-divisible subset
def non_div_subset():
    # Input
    n, k = map(int, input().rstrip().split())
    s = list(map(int, input().rstrip().split()))

    # Function
    rest = [0 for _ in range(k)]
    for i in s:
        rest[i % k] += 1
    max_n = 1 if rest[0] > 0 else 0
    for i in range(1, k // 2 + 1):
        if i != k - i:
            max_n += max(rest[i], rest[k - i])
        else:
            max_n += 1
    print(max_n)


# Equalize the Array
def equalize_array():
    # Input
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    # Function
    result = n - max([arr.count(e) for e in set(arr)])
    print(result)


# Queen's attack II
def queen_attack_2():
    # Input
    n, k = map(int, input().rstrip().split())
    rq, cq = map(int, input().rstrip().split())  # row and col for queen
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    # Function
    max_attacks = [
        min(rq - 1, cq - 1),
        cq - 1,
        min(n - rq, cq - 1),
        n - rq,
        min(n - rq, n - cq),
        n - cq,
        min(rq - 1, n - cq),
        rq - 1,
    ]
    for ro, co in obstacles:
        if ro - rq == co - cq:
            if ro < rq:
                max_attacks[0] = min(max_attacks[0], rq - ro - 1)
            else:
                max_attacks[4] = min(max_attacks[4], ro - rq - 1)
        elif ro == rq:
            if co < cq:
                max_attacks[1] = min(max_attacks[1], cq - co - 1)
            else:
                max_attacks[5] = min(max_attacks[5], co - cq - 1)
        elif ro - rq == cq - co:
            if co < cq:
                max_attacks[2] = min(max_attacks[2], cq - co - 1)
            else:
                max_attacks[6] = min(max_attacks[6], co - cq - 1)
        elif co == cq:
            if rq < ro:
                max_attacks[3] = min(max_attacks[3], ro - rq - 1)
            else:
                max_attacks[7] = min(max_attacks[7], rq - ro - 1)
    result = sum(max_attacks)
    print(result)


# ACM ICPC Team
def acm_icpc_team():
    # Input
    n, m = map(int, input().rstrip().split())
    topic = [input() for _ in range(n)]

    # Function
    quantities = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = str(int(topic[i]) + int(topic[j]))
            quantities.append(len(x) - x.count("0"))
    result = max(quantities), quantities.count(max(quantities))
    print("\n".join(map(str, result)))


# Taum and B'day
def taum_bday():
    # Input
    t = int(input())
    for _ in range(t):
        b, w = map(int, input().rstrip().split())
        bc, wc, z = map(int, input().rstrip().split())
        # Function
        result = b * min(bc, wc + z) + w * min(wc, bc + z)
        # End function
        print(result)


# Organizing containers of balls
def organizer_container_balls():
    # Input
    for _ in range(int(input())):
        container = [
            list(map(int, input().rstrip().split())) for _ in range(int(input()))
        ]
        # Function
        r = sorted([sum(x) for x in container])
        c = sorted([sum(x) for x in zip(*container)])
        result = "Possible" if r == c else "Impossible"
        print(result)


# Encryption
def encryption():
    # Input
    s = input()

    # Function
    s = s.replace(" ", "")
    qr = math.floor(len(s) ** 0.5)
    qc = math.ceil(len(s) ** 0.5)
    if qr * qc < len(s):
        qr += 1
    result = ""
    for i in range(qc):
        result += s[i::qc] + " "
    print(result)


# Bigger is Greater
def bigger_is_greater(w):
    word = list(w)
    p = len(w) - 2
    while p >= 0 and word[p] >= word[p + 1]:
        p -= 1
    print(p)
    if p == -1:
        return "no answer"
    for i in range(len(word) - 1, p, -1):
        if word[i] > word[p]:
            word[i], word[p] = word[p], word[i]
            break
    word[p + 1 :] = reversed(word[p + 1 :])
    return "".join(word) if "".join(word) != w else "no answer"


def bigger_greater():
    # Input
    for _ in range(int(input())):
        w = input()
        # Function
        s = bigger_is_greater(w)
        print(s)


# Modified Kaprekar Numbers
def kaprekar_numbers():
    # Input
    p = int(input())
    q = int(input())

    # Function
    arr = []
    for i in range(p, q + 1):
        s = str(i ** 2)
        if len(s) == 1:
            s = "0" + s
        if int(s[: math.floor(len(s) / 2)]) + int(s[-math.ceil(len(s) / 2) :]) == i:
            arr.append(i)
    result = "INVALID RANGE" if arr == [] else " ".join(map(str, arr))
    print(result)


# Beautiful triplets
def beautiful_triplets():
    # Input
    n, d = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    # Function
    result = sum(a + d in arr and a + d + d in arr for a in arr)
    print(result)


# Minimum distances
def min_distances():
    # Input
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    # Function
    arr = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                arr.append(j - i)
    result = min(arr) if len(arr) > 0 else -1
    print(result)


# Halloween Sale
def halloween_sale():
    # Input
    p, d, m, s = map(int, input().rstrip().split())

    # Function
    result = 0
    while s >= p:
        s -= p
        result += 1
        p -= d
        if p < m:
            p = m
    print(result)


# The time in words
def time_in_words():
    # Input
    h = int(input())
    m = int(input())

    # Function
    hours = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
    ]
    minutes = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
    ]
    result = ""

    if m == 0:
        result = hours[h] + " o' clock"
    elif m % 30 == 0:
        result = "half past " + hours[h]
    elif m % 15 == 0:
        result = "quarter "
        result += ("past " + hours[h]) if m < 30 else ("to " + hours[h + 1])
    else:
        result = "{0} minute{1} {2} {3}".format(
            minutes[m if m < 30 else (60 - m)],
            "" if m == 1 else "s",
            "past" if m < 30 else "to",
            hours[h] if m < 30 else hours[h + 1],
        )
    print(result)


# Chocolate Feast
def chocolate_feast():
    # Input
    t = int(input())
    for _ in range(t):
        n, c, m = map(int, input().rstrip().split())
        # Function
        w = n // c
        k = w
        while w // m > 0:
            k += w // m
            w = w // m + w % m
        print(k)


# Service Lane
def service_lane():
    # Input
    n, t = map(int, input().rstrip().split())
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    # Function
    result = [min(width[i : j + 1]) for i, j in cases]
    # End function
    print("\n".join(map(str, result)))


# Lisa's Workbook
def lisas_workbook():
    # Input
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    # Function
    p = 0
    special_problems = 0
    for i in range(n):
        pages_in_chapter = math.ceil(arr[i] / k)
        for j in range(1, pages_in_chapter + 1):
            if (j * k - k + 1) <= p + j <= (j * k if j * k < arr[i] else arr[i]):
                special_problems += 1
        p += pages_in_chapter
    print(special_problems)


# Flatland Space Stations
def flatland_space_stations():
    # Input
    n, m = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))

    # Function
    c = sorted(c)
    result = max([(c[i + 1] - c[i]) // 2 for i in range(m - 1)]) if m > 1 else 0
    result = max(result, c[0], n - 1 - c[m - 1])
    print(result)


# Fair Rations
def fair_rations():
    # Input
    n = int(input())
    b = list(map(int, input().rstrip().split()))

    # Function
    odd = [i for i in range(n) if b[i] % 2]
    if len(odd) % 2 == 0:
        result = sum([(odd[i + 1] - odd[i]) * 2 for i in range(0, len(odd), 2)])
    else:
        result = "NO"
    print(result)


# Cavity Map
def cavity_map():
    # Input
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input())

    # Funstion
    for i in range(1, n - 1, 1):
        for j in range(1, n - 1, 1):
            if grid[i][j] > max(
                grid[i][j - 1], grid[i][j + 1], grid[i - 1][j], grid[i + 1][j]
            ):
                grid[i] = grid[i][:j] + "X" + grid[i][j + 1 :]
    print("\n".join(grid))


# Manasa and Stones
def manasa_stones():
    # Input
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = int(input())
        b = int(input())
        # Function
        result = sorted(set([(a * (n - 1 - i) + b * i) for i in range(n)]))
        print(result)


# The Grid Search
def grid_search():
    # Input
    t = int(input())
    for _ in range(t):
        R, C = map(int, input().rstrip().split())
        G = [input() for _ in range(R)]
        r, c = map(int, input().rstrip().split())
        P = [input() for _ in range(r)]
        # Function
        result = "NO"
        sp = "".join(P)
        for i in range(len(G) - len(P) + 1):
            for j in range(len(G[i]) - len(P[0]) + 1):
                if G[i][j : j + len(P[0])] == P[0]:
                    x = "".join([G[i + k][j : j + len(P[0])] for k in range(len(P))])
                    if x == "".join(P):
                        result = "YES"
        print(result)


# Happy Ladybugs
def happy_ladybugs():
    # Input
    g = int(input())
    for _ in range(g):
        n = int(input())
        b = input()
        # Function
        result = "YES"
        for i in set(b):
            if i != "_" and b.count(i) == 1:
                result = "NO"
        if "_" not in b:
            for i in range(1, len(b) - 1):
                if b[i - 1] != b[i] and b[i] != b[i + 1]:
                    result = "NO"
        print(result)


# Strange Counter
def strange_counter():
    # Input
    t = int(input())

    # Function
    result = 3 * 2 ** math.ceil(math.log2(t / 3 + 1)) - t - 2
    print(result)


# 3D surface area
def surface_3d_area():
    # Input
    h, w = map(int, input().rstrip().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(h)]

    # Function
    area = 2 * len(arr) * len(arr[0])
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            area += arr[i][j] if i == 0 else max(0, arr[i][j] - arr[i - 1][j])
            area += (
                arr[i][j] if i == len(arr) - 1 else max(0, arr[i][j] - arr[i + 1][j])
            )
            area += arr[i][j] if j == 0 else max(0, arr[i][j] - arr[i][j - 1])
            area += (
                arr[i][j] if j == len(arr[0]) - 1 else max(0, arr[i][j] - arr[i][j + 1])
            )
    print(area)


# Absolute Permutation
def absolute_permutation():
    # Input
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        # Function
        if k == 0:
            perm = list(range(1, n + 1))
        elif (n / k) % 2 != 0:
            perm = ["-1"]
        else:
            add = True
            perm = []
            for i in range(1, n + 1):
                perm.append((i + k) if add else (i - k))
                if i % k == 0:
                    add = not add
        print(*perm)


# Matrix layer rotation
def matrix_layer_rotation():
    # Input
    m, n, r = map(int, input().rstrip().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split()))[:n])
    print(matrix)
    # Function
    """
    need_rotation = m % 2 != 0
    if need_rotation:
        matrix = list(zip(*matrix))[::-1]
    print_matrix2D(matrix)
    for _ in range(len(matrix) // 2):
        for i in range()
    if need_rotation:
        matrix = list(zip(*matrix[::-1]))
    print_matrix2D(matrix)
    """
    # Passing all rings of rotation
    for z in range(min(m, n) // 2):
        # Loading elements of a ring of revolution into a one-dimensional list
        lst_straight = []
        lst_reverse = []
        for i in range(m - z * 2):
            for j in range(n - z * 2):
                if i == 0:
                    lst_straight.append(matrix[i + z][j + z])
                elif i == m - z * 2 - 1:
                    lst_reverse.append(matrix[i + z][j + z])
                elif j == n - z * 2 - 1:
                    lst_straight.append(matrix[i + z][j + z])
                elif j == 0:
                    lst_reverse.append(matrix[i + z][j + z])
        lst = lst_straight + list(reversed(lst_reverse))
        # Shift elements of the ring of rotation by r positions counterclockwise
        lst = lst[r % len(lst) :] + lst[: r % len(lst)]
        # Backloading shifted elements from a rotation ring into a 2D array
        lst_straight = lst[: len(lst) // 2]
        lst_reverse = list(reversed(lst[len(lst) // 2 :]))
        for i in range(m - z * 2):
            for j in range(n - z * 2):
                if i == 0:
                    matrix[i + z][j + z] = lst_straight.pop(0)
                elif i == m - z * 2 - 1:
                    matrix[i + z][j + z] = lst_reverse.pop(0)
                elif j == n - z * 2 - 1:
                    matrix[i + z][j + z] = lst_straight.pop(0)
                elif j == 0:
                    matrix[i + z][j + z] = lst_reverse.pop(0)
    # Print matrix 2D
    for elem in matrix:
        print(" ".join(map(str, elem)))


absolute_permutation()
