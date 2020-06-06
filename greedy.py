def maximumToys():
    # Input maximum toys
    k = 50
    s = "1 12 5 111 200 1000 10"
    prices = list(map(int, s.rstrip().split()))

    # Function maximum toys
    count_max = 0
    basket = 0
    prices.sort()
    print(prices)
    for p in prices:
        if basket + p < k:
            basket += p
            count_max += 1
        else:
            break
    print(count_max)
    return count_max
