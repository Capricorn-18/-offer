class Solution:
    def numWays(self, n: int, relation, k: int) -> int:
        dp = [[0]*n for _ in range(k+1)]
        dp[0][0] = 1

        for t in range(k):
            for x, y in relation:
                dp[t+1][y] += dp[t][x]
        return dp[k][n-1]