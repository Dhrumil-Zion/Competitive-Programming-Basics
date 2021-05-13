nums1 = []
nums2 = [2]
final_arr = nums1+nums2
final_arr.sort()
index = int(len(final_arr)/2)
print(final_arr)
if len(final_arr)%2==0:
    print("{:.5f}".format((final_arr[index]+final_arr[index-1])/2))
else:
    print("{:.5f}".format(final_arr[index]))