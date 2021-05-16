arr = [int(g) for g in input().split()]
element = int(input())
if element not in arr:
    print(-1)
else:
    print("{} is at index {}".format(element,arr.index(element)))
