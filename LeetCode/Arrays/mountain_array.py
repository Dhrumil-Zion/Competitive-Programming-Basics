def mountain(arr):
    temp = sorted(arr)
    if arr==temp:
        return False
    temp.reverse()
    if arr==temp:
        return False

    try:
        for c in range(len(arr)):
            if arr[c]<arr[c+1]:
                continue
            else:
                for v in range(c+1,len(arr)+1):
                    if v==len(arr):
                        return True
                    if arr[v]<arr[v-1]:
                        continue
                    else:
                        return "False"
        return True
    except:
        return False


v = [2,0,2]
# [0,1,2,3,4,8,9,10,11,12,11]
print(mountain(v))