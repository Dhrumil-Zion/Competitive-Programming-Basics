arr = [1 ,2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
my_dict = {}
uni = set(arr)
for x in uni:
    my_dict[x] = arr.count(x)

my_dict.fo
print(my_dict.values())










# for x in uni:
#     a.append(arr.count(x))
# for x in range(len(uni)):
#     max_index = arr.index(max(a))
#     if x ==0:
#         b.append(a[max_index])
#         a.pop(max_index)
#     else:
#         if b[x-1] > a[max_index]:
#             break
#         else:
#            b.append(a[max_index]) 
#            a.pop(max_index)  
# b.sort()
# print(b[0])                
