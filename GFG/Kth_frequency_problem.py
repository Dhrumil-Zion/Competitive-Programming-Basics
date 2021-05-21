"""
Geek hosted a coding competition, some of the questions were easy and some of them were hard.
You are given an array arr of positive integers of size N and an integer K, arr[i] represents the 
hardness of each problem of geeks' contest. Among those N numbers, your task is to find the numbers 
which appear more than K times and print them in increasing order. If no number appears more than K 
times than print -1.

Input:
1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
2. The first line of each test case contains two space-separated integers N and K.
3. The second line contains N space-separated positive integers represents array arr.

Example:
Input:
3
3 1
5 5 6
6 1
2 2 3 3 4 4
4 2
1 2 2 3

Output:
5
2 3 4
-1

"""

T = int(input())
answer = []
while(T > 0):
    ans=[]
    a = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    l = a[0]
    k = a[1]
    f_arr = arr[:l]
    prop = set(f_arr)
    for x in prop:
        if f_arr.count(x) > k:
            ans.append(x)        
    if len(ans) == 0:
        answer.append([0,-1])
    else:
        ans.sort()
        answer.append(ans)                        
    T = T - 1

for s in answer:
    for y in s:
        if y == 0:
            continue
        print(y,end=" ")
    print("")        