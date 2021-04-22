## https://practice.geeksforgeeks.org/problems/minimum-sum-of-subarray/0/

T = int(input())
l = []
while T!=0:
    ans = ""
    le = int(input())
    arr = [int(f) for f in input().split()]
    
    for c in range(le):
        final_arr_arr = arr[c:]
        k = [final_arr_arr[i:i+j] for i in range(len(final_arr_arr)) for j in range(1,len(final_arr_arr)-i+1)]
        z = [sum(c) for c in k]
        ans = ans + str(min(z)) + " "
    l.append(ans)
    T-=1
for v in l:
    print(v)

