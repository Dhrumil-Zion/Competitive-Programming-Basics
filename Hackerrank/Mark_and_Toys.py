def maximumToys(prices, k):
    prices.sort()
    c=0
    while(1):
        if sum(prices[:c+1]) >=k:
            break
        else:
            c+=1
    return c