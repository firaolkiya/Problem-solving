directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
def inbound(row, col):
    return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
def dfs(grid, visited, row, col):
 # base case
    visited[row][col] = True
    for row_change, col_change in directions:
        new_row = row + row_change
        new_col = col + col_change
        if inbound(new_row, new_col) and not visited[new_row][new_col]:
            dfs(grid, visited, new_row, new_col)

def dfs(node):
    if node == destination:
        return True
    for neighbour in graph[node]:
        found = dfs(neighbour)
        if found:
            return True
    return False