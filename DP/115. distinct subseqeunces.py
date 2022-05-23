# 以t为中心，依次查看s中的字符是否满足条件
# len(s)=m len(t)=n, 复杂度O(n*m^2)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dp(s, i, t, j):
            if len(t) == j:
                return 1
            if len(s) - i < len(t) - j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            res = 0
            for k in range(i, len(s)):
                if s[k] == t[j]:
                    res += dp(s, k + 1, t, j + 1)

            memo[i][j] = res
            return res

        memo = [[-1] * len(t) for _ in range(len(s))]
        return dp(s, 0, t, 0)