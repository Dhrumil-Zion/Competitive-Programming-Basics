def singleNumber(nums):
    theNumber = nums[0]             # Store the 1st number of the list in the resultant variable, 'theNumber'
    for i in range(1, len(nums)):   # Traverse from the 2nd to the last number of the list
        theNumber ^= nums[i]        # Add update 'theNumber' by doing XOR with the ith number of the list
    return theNumber 

print(singleNumber([1,2,2,3,3,5,1]))