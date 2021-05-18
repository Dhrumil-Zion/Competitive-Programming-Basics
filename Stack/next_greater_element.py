# nums1=[1,3,5,2,4]
# nums2=[6,5,4,3,2,1,7]

# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
# nums1 = [2,4]
# nums2 = [1,2,3,4]
nums1 =[4,1,2]
nums2 =[1,2,3,4]


### Optimized one

A =[4,1,2]
B =[1,2,3,4]
stack = []
diff = {}

for pos, val in enumerate(B): 
    while stack and stack[-1] < val:
        diff[stack.pop()] = val
    stack.append(val)
for pos in range(len(A)):
    A[pos] = diff.get(A[pos], -1)
print( A)


# temp =[]
# temp2=[]
# for f in nums1:
#     idx =nums2.index(f)
#     if idx==len(nums2)-1:
#         temp.append(-1)
#     elif f < max(nums2[idx+1:]):
#         for c in nums2[idx+1:]:
#             if f<c:
#                 temp2.append(c)
#         temp.append(temp2[0])
#         temp2.clear()
#     else:
#         temp.append(-1)
# print(temp)
