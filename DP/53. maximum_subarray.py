# dp思想，dp[i-1]为以nums[i-1] 结尾的最大子序列的和， 如果大于0,dp[i] = dp[i-1]+nums[i]，小于0, 从dp[i] = nums[i]开始重记


class Solution:
    def maxSubArray(self, nums) -> int:
        _sum = 0
        res = nums[0]
        for num in nums:
            if _sum < 0:
                _sum = num
            else:
                _sum += num
            res = max(_sum, res)
        return res


if __name__ == '__main__':
    Solution().maxSubArray([5,4,-1,7,8])