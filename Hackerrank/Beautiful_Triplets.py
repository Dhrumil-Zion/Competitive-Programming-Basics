def beautifulTriplets(d, arr):
    return sum(
        arr.count(i) * arr.count(i + d) * arr.count(i + 2 * d)
        for i in list(set(arr))
    )