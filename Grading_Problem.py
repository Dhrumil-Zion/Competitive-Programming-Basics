grades = [73,67,38,33]
for x in range(len(grades)):
        temp = grades[x] 
        t=grades[x]
        if grades[x]<38:
            continue
        while t%5!=0:
            t +=1
        if (t - temp) < 3:
            grades[x]=t
print(grades)