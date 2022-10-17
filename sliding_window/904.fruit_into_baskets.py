#  本题实际上是求最多包含两个元素的最长连续子序列
#  用滑动窗口做
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        l, ans, typ = 0, 0, 0
        dict_ = defaultdict(int)

        for r in range(len(fruits)):
            dict_[fruits[r]] += 1
            if dict_[fruits[r]] == 1:
                typ += 1
            while typ > 2:
                dict_[fruits[l]] -= 1
                if dict_[fruits[l]] == 0:
                    typ -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans