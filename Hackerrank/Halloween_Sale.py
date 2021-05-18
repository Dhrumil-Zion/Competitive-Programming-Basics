def howManyGames(p, d, m, s):
    budget = s
    price = p
    deduction = d
    minprice = m
    c=0
    while 1:
        budget = budget - price
        if budget>=0:
            price = price -deduction
            if price>minprice:
                c+=1
                continue
            else:
                if budget >= price-minprice:
                    c+=1
                    price = minprice
                else:
                    break
        else:
            break
    return c