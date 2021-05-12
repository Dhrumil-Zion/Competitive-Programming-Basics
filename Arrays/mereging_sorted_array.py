nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

temp1 = nums1[:m]
temp2 = nums2[:n]
temp = temp1+temp2
temp.sort()
print(temp)


# for c in range(len(nums1)-m):
#     nums1.pop()

# for v in range(len(nums2)-n):
#     nums2.pop()
    
# for f in range(len(nums2)):
#     nums1.append(nums2[f])
# nums1.sort()