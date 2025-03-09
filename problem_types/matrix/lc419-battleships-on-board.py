class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:

        rows = len(board)
        cols = len(board[0])
        count = 0

        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):

            print(r,c)

            if (r > rows - 1) or (c > cols - 1) or board[r][c] != 'X' or visited[r][c]:
                return

            visited[r][c] = True

            dfs(r + 1, c)
            dfs(r, c + 1)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X' and not visited[r][c]:
                    count += 1
                    dfs(r,c)
        
        return count 
