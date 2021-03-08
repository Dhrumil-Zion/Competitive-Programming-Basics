"""
Link = https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

def method_3(s,t,a,b,apples,oranges):          #### Optimized Code ####
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))

def method_4(s,t,a,b,apples,oranges):           #### Optimized Code ####
    print(sum(s <= a + d <= t for d in apples))
    print(sum(s <= b + d <= t for d in oranges))

def method_1(s,t,a,b,apples,oranges):           #### time Complexity exceeds in GFG Code ####
    house_arr =[]
    temp = s
    count_apples =0
    count_oragnes =0
    y = (t-s)+1
    le_app = 0 
    x = 0
    if len(apples) >= len(oranges):
        le_app = len(apples)
    else:
        le_app = len(oranges)    
    while(y!=0):
        house_arr.append(temp)
        temp +=1
        y -=1
    while le_app!=0:
        if x != len(apples):
            apples[x] = apples[x] + a
            if apples[x] in house_arr:
                count_apples +=1
        if x != len(oranges):
            oranges[x] = oranges[x] + b
            if oranges[x] in house_arr:
                count_oragnes +=1
        x +=1
        le_app -=1           
    print(count_apples)
    print(count_oragnes)          

def method_2(s,t,a,b,apples,oranges):               #### time Complexity exceeds in GFG Code ####
    house_arr =[]
    temp = s
    count_apples =0
    count_oragnes =0
    for x in range((t-s)+1):
        house_arr.append(temp)
        temp +=1
    print(house_arr)    
    for x in range(len(apples)):
        apples[x] = apples[x] + a
        if apples[x] in house_arr:
            count_apples +=1        
    for x in range(len(oranges)): 
        oranges[x] = oranges[x] + b
        if oranges[x] in house_arr:
            count_oragnes +=1
    print("{} {}".format(count_apples,count_oragnes))        


s = 7 
t = 11
a =5
b =15
apples = [-2,2,1]
oranges = [5,-6]
# method_1(s,t,a,b,apples,oranges)
# method_2(s,t,a,b,apples,oranges)
method_3(s,t,a,b,apples,oranges)
method_4(s,t,a,b,apples,oranges)



