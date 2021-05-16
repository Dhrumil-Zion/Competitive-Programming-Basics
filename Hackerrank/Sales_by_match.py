def sockMerchant(n, ar):
    final = set(ar)
    count  =0
    a = [ar.count(x) for x in final]
    for x in a:
        if x==1:
            continue
        if x>1:
            count += int(x/2)
    return count    