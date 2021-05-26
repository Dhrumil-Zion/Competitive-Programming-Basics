def checkStraightLine(coordinates):    
    if len({x for x, y in coordinates}) == 1: return True
    if len({x for x, y in coordinates}) < len(coordinates): return False
    return (
        len(
            {
                (p1[1] - p2[1]) / (p1[0] - p2[0])
                for p1, p2 in zip(coordinates, coordinates[1:])
            }
        )
        == 1
    )

arr = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(arr))









# below solution gives divide by zero error
# slop = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
# for c in range(2,len(coordinates)):
#     if (coordinates[c][1]-coordinates[c-1][1])/(coordinates[c][0]-coordinates[c-1][0]) == slop:
#         continue
#     else:
#         return False
# return True