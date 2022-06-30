class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0]*n for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = i
        for j in range(1, n):
            dp[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] ==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 三种情况
                    # dp[i-1][j-1]+1  word1[i] 替换成 word2[j]
                    # dp[i-1][j]+1  删除了word1[i]
                    # dp[i][j-1]+1  加入了word1[i] = word2[j]
                    dp[i][j] = min(dp[i-1][j]+1, min(dp[i][j-1]+1, dp[i-1][j-1]+1))
        return dp[-1][-1]