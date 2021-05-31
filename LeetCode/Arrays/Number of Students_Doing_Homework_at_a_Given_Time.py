startTime = [1,1,1,1]
endTime = [1,3,2,4]
queryTime = 7
count = sum(s<= queryTime <=e for s,e in zip(startTime,endTime))
print(count)