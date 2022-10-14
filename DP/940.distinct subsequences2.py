class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [[0, 0] for _ in range(n)]
        # 初始化 0是不选择 1是选择
        dp[0][0] = 0
        dp[0][1] = 1

        for i in range(1, n):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % (10 ** 9 + 7)
            dp[i][1] = (dp[i-1][0] + dp[i-1][1] + 1) % (10 ** 9 + 7)
            for j in range(i-1, -1, -1):
                # 去重
                if s[j] == s[i]:
                    dp[i][1] -= dp[j][1]
        return (dp[-1][0] + dp[-1][1]) % (10 ** 9 + 7)

