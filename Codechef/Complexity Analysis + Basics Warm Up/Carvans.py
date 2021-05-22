# Problem Name: Carvans 
# Problem Code: CARVANS

for _ in range(int(input())):
    n = int(input())
    cars = list(map(int, input().split()))
    r = 1
    for j in range(1, n):
        if cars[j] < cars[j - 1]:
            r += 1
        else:
            cars[j] = cars[j - 1]
    print(r)