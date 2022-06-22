# dp O(N^2)
# dp[i]代表 nums[i]结尾的最长上升子序列长度
# 循环nums[:i-1]不断覆盖dp[i]的最大值
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) < 2:
            return len(nums)
        dp = [1] * len(nums)
        result = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        return result

# 二分法 O(NlogN)
# 对原序列进行遍历，将每位元素二分插入 cell 中。
#
# 如果 cell 中元素都比它小，将它插到最后
# 否则，用它覆盖掉比它大的元素中最小的那个。
#  https://leetcode.cn/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-e/
class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)
        cur = [nums[0]]

        for num in nums[1:]:
            if num > cur[-1]:
                cur.append(num)
                continue
            l,r = 0, len(cur)-1
            while l < r:
                mid = l + (r-l)//2
                if cur[mid] >= num:
                    r = mid
                else:
                    l = mid+1
            cur[l] = num
        return len(cur)