# https://www.hackerrank.com/challenges/cavity-map/problem

grid = ['1112', '1912', '1892', '1234']
# temp = [max(list(c)) for c in grid]
# final = []
# for f in grid:
#    if max(temp) in f:
#        final.append(f.replace(str(max(temp)), 'X'))
#    else:
#        final.append(f)
#print(final)

n = len(grid)
for i in range(1,n-1):
	for j in range(1,n-1):
    		if grid[i][j] > max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
        		grid[i] = grid[i][:j] +'X' + grid[i][j+1:]
print(grid)       
