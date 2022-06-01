# 定义s[i..] 的子序列中 t[j..] 出现的次数为 dp(s, i, t, j)

# 以t为中心, 依次查看s中的字符是否满足条件
# len(s)=m len(t)=n, 复杂度O(n*m^2)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dp(s, i, t, j):
            # 走到边界说明找到一种相等的组合
            if len(t) == j:
                return 1
            # 剩下s的字符长度小于t, 肯定不存在这种组合
            if len(s) - i < len(t) - j:
                return 0
            # 已经记录的直接返回
            if memo[i][j] != -1:
                return memo[i][j]

            res = 0
            for k in range(i, len(s)):
                if s[k] == t[j]:
                    res += dp(s, k + 1, t, j + 1)

            memo[i][j] = res
            return res

        # 消除重叠子问题
        memo = [[-1] * len(t) for _ in range(len(s))]
        return dp(s, 0, t, 0)

# 以s为中心, 看s的每个字符能否和t中的字符匹配
# len(s)=m len(t)=n, 复杂度O(n*m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dp(s, i, t, j):
            if j == len(t):
                return 1
            if len(s) - i < len(t) - j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            res = 0
            # 如果当前字符相等,可以选择匹配s[i]或者放过s[i]
            if s[i] == t[j]:
                res += dp(s, i+1, t, j+1) + dp(s, i+1, t, j)
            # 如果不相等,只能放过当前s[i]
            else:
                res += dp(s, i+1, t, j)

            memo[i][j] = res
            return res
        memo = [[-1]*len(t) for _ in range(len(s))]
        return dp(s, 0, t, 0)