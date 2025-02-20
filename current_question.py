# Just a random python file for any testing you might have
# Think of this as replit

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        visited = [[False] * cols for _ in range(rows)]

        # will explore the graph and mark things visited, but once we reach water we stop
        def dfs(i, j):
            for i in range(rows):
                for j in range(cols):

                    visited[i][j] = True

                    if (j >= cols or grid[i][j+1] == "0" or visited[i][j+1]) and (j < 0 or grid[i][j-1] == "0" or visited[i][j-1] ) and (i >= rows or grid[i+1][j] == "0" or visited[i+1][j]) and (i < 0 or grid[i-1][j] == "0" or visited[i-1][j]):
                        break
                    

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(i, j)

        return res

s = Solution()

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

s.numIslands(grid)