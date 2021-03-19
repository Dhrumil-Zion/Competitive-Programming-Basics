def howManyGames(p, d, m, s):
    budget = s
    price = p
    deduction = d
    minprice = m
    c=0
    while(1):
        budget = budget - price
        if budget>=0:
            price = price -deduction
            if price>minprice:
                c+=1
                continue
            elif price<=minprice:
                if budget >= price-minprice:
                    c+=1
                    price = minprice
                else:
                    break    
        else:
            break        
    print(c)        

p = 20 
d = 3 
m = 6 
s = 85

howManyGames(p, d, m, s)