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

[Review Union Find](/algorithms/union-find/union-find.md)

- We union each island cell if the neighbor is also an island to form an island.
- We need to create a UnionFind class to create find and union functions.

```
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        count = 0
        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1":
                    count += 1

                    x1 = i * n + j

                    if i + 1 <= m - 1 and grid[i+1][j] == "1":
                        x2 = x1 + n
                        count -= uf.union(x1, x2)
                    
                    if j + 1 <= n - 1 and grid[i][j + 1] == "1":
                        x2 = x1 + 1
                        count -= uf.union(x1, x2)

        return count
```

Explanation of logic:

Given an example grid

1 1 0
1 0 1
0 1 1

Following this code

```
if grid[i][j] == "1":
    count += 1

    x1 = i * n + j
```

At grid[0][0] `x1 = i + n * j` , we have:
- i = 0 which is the current row
- n = 3 which is the wdith of the grid
- j = 0 which is the current col position

Since we instantiated parent as a 1D array, we need to be able to differentiate between the different rows:

```
(0,0) (0,1) (0,2)    0  1  2
(1,0) (1,1) (1,2) -> 3  4  5
(2,0) (2,1) (2,2)    6  7  8
```

So to map the following grid indices we have:

- (0,0) → 0 * 3 + 0 = 0
- (0,1) → 0 * 3 + 1 = 1
- (1,0) → 1 * 3 + 0 = 3
- (1,1) → 1 * 3 + 1 = 4

Which means that for any multiple of 3 in the 1D array represents a row in the original 2D grid.

Then taking the next code snippet:

```
if i + 1 <= m - 1 and grid[i+1][j] == "1":
    x2 = x1 + n
    count -= uf.union(x1, x2)
```

We check if the gird space below is out of bounds and if it is an island.

All `x2 = x1 + n` does is move the pointer below the current one.

count increases by each new "1" however, it will decrease if we realize that those 1s are connected or
in other words, the union was sucessful.

- "if there's a 1 next to me or below me, we're part of the same island, so let's union them together."