inp1 = [int(x) for x in input().split()]
inp2 = [int(x) for x in input().split()]
l1 = inp1[0]
l2 = inp1[1]
final_arr = inp2[:l2]
arr  = []
count = 0

print(final_arr)
for x in range(l1):
    arr.append(0)

for y in final_arr:
    for x in range(l1):
        if y >= arr[x]:
            arr[x] +=1
print(arr)            