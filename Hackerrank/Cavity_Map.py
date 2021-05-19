def cavityMap(grid):
    n = len(grid)
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i][j] > max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
                grid[i] = grid[i][:j] +'X' + grid[i][j+1:]
                
    return grid
