# 4
#  13 7 6 12
# sourcery skip: min-max-identity
num = int(input())
marks = list(map(int,input().split()))
marks = marks[:num]
for ind in range(len(marks)):
    if ind==len(marks)-1:
        continue
    if marks[ind]<max(marks[ind+1:]):
        marks[ind]=max(marks[ind+1:])
print(*marks)