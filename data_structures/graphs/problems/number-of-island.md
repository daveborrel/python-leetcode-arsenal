# Number of Islands

- This combines the technique of traversing a 2d array and graph traversal.
- When using DFS
    - think in recursions and not loops
    - mark visited before exploring anything else
    - check if the current cell is invalid or not - if it is, return it ASAP.

![image](/data_structures/graphs/asset/islands.png)

## DFS Approach

- DFS Failed Approach

- attempt #1 this fails because
    - you're doing a nested loop inside of dfs which defeats the purpose of doing a dfs

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        visited = [[False] * cols for _ in range(rows)]

        # will explore the graph and mark things visited, but once we reach water we stop
        def dfs(i, j):
            for i in range(rows):
                for j in range(cols):

                    visited[i][j] = True

                    if ((j+1 >= cols or grid[i][j+1] == "0" or visited[i][j+1]) and
                       (j-1 < 0 or grid[i][j-1] == "0" or visited[i][j-1] ) and
                       (i+1 >= rows or grid[i+1][j] == "0" or visited[i+1][j]) and
                       (i-0 < 0 or grid[i-1][j] == "0" or visited[i-1][j])):
                        break
                    

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(i, j)

        return res
```

- Even in this version, if you use the passed in parameters like r and c, you're still doing a grid search which is not dfs.

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        visited = [[False] * cols for _ in range(rows)]

        # will explore the graph and mark things visited, but once we reach water we stop
        def dfs(r, c):
            for i in range(r, rows):
                for j in range(c, cols):

                    visited[i][j] = True

                    if ((j+1 >= cols or grid[i][j+1] == "0" or visited[i][j+1]) and
                       (j-1 < 0 or grid[i][j-1] == "0" or visited[i][j-1] ) and
                       (i+1 >= rows or grid[i+1][j] == "0" or visited[i+1][j]) and
                       (i-0 < 0 or grid[i-1][j] == "0" or visited[i-1][j])):
                        break
                    

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(i, j)

        return res
```

- Proper DFS

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        visited = [[False] * cols for _ in range(rows)]

        # will explore the graph and mark things visited, but once we reach water we stop
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or visited[r][c]:
                return
            
            visited[r][c] = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
                    

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(i, j)

        return res
```


## Union Find Approach

- We union each island cell if the neighbor is also an island to form an island.
- We need to create a UnionFind class here.

```
```