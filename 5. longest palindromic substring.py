# 从中间向两边扩散判断是否为回文串
# 时间复杂度O(n^2), 空间复杂度O(1)
class Solution:
    def longestPalindrome(self, s):
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        if len(s) < 2:
            return s
        res = ''
        for i in range(len(s)):
            # 判断以s[i]为中心的回文串
            t1 = palindrome(s, i, i)
            # 判断以s[i] s[i+1]为中心的回文串
            t2 = palindrome(s, i, i + 1)
            if len(res) < len(t1):
                res = t1
            if len(res) < len(t2):
                res = t2
        return res

# 动态规划
# 时间复杂度O(n^2), 空间复杂度O(n^2)
# dp[i][j]判断s[i:j+1]是否是回文子串
# when dp[i+1][j-1] and s[i]==s[j], dp[i][j]=True
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        res = ''
        l, r = 0, 0
        dp = [[False]*n for _ in range(n)]

        # dp[i]依赖dp[i+1],倒序遍历
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif i == j-1 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                if dp[i][j] and r-l < j-i:
                    l,r = i,j
        return s[l:r+1]
