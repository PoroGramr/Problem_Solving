class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:

        dy = [-1,0]
        dx = [0,-1]

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for k in range(m):
            dp[k][0] = 1
        for s in range(n):
            dp[0][s] = 1

        for y in range(1,m):
            for x in range(1,n):
        
                if (x + dx[0]) >= 0 and (y + dy[0]) >= 0:
                    dp[y][x] += dp[y +dy[0]][x + dx[0]]
                if (x + dx[1] >= 0) and (y +dy[1]) >= 0:
                    dp[y][x] += dp[y + dy[1]][x + dx[1]]

        return dp[m-1][n-1]

        
