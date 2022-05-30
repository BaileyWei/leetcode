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