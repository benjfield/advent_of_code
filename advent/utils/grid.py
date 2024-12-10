def check_inbounds(grid, x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)