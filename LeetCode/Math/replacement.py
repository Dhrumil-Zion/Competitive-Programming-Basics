num = 9669

## one liner

i = 9999
c= int(str(i).replace('6', '9',1))
print(c)

## optimized one

can_change = True
result = ''
for n in str(num):
    if can_change:
        result += '9'
        if n == '6': can_change = False
    else:
        result += n
print(result)



# temp=[int(f) for f in str(num)]
# k=0
# for v in range(len(temp)):
#     if k==1:
#         break
#     if temp[v]==9:
#         continue
#     temp[v]=9
#     k+=1
# print(temp)
