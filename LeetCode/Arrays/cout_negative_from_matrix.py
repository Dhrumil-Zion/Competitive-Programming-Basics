grid = [[-1]]
k=0
for v in grid:
    v.sort()
    for b in v:
        if b<0:
            k+=1
            continue
        break
print(k)

## more optimized below

# neg_counter = 0
# column_num = len(grid[0])
# row_num = len(grid)
# last_positive_column = column_num
# for row_idx in range(row_num):
#     for column_idx in range(last_positive_column):
#         if grid[row_idx][column_idx] < 0:
#             negs = (row_num - row_idx) *(last_positive_column-column_idx)
#             neg_counter += negs
#             last_positive_column = column_idx
#             break
# print(neg_counter) 