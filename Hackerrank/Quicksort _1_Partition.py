def quickSort(arr):
    left = []
    right = []
    equal = [arr[0]]
    for x in arr:
        if x == arr[0]:
            continue
        elif x < arr[0]:
            left.append(x)
        elif x > arr[0]:
            right.append(x)
    return (left+equal+right) 