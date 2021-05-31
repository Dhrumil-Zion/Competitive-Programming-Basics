startTime = [1,1,1,1]
endTime = [1,3,2,4]
queryTime = 7
count = 0
for s,e in zip(startTime,endTime):
    if s<= queryTime <=e:
        count+=1
print(count)