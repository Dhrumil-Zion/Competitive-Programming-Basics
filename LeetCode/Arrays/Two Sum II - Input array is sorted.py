def twoSum(numbers, target):
    num_set = {}
    for i in range(len(numbers)):
        difference = target - numbers[i]
        try:
            num_set[difference]
            return [num_set[difference], i + 1]
        except KeyError:
            num_set[numbers[i]] = i + 1

print(twoSum([2,7,11,15],9))