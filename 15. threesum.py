"""
重点在如何去重
排序+双指针
"""


class Solution:
    def threeSum(self, nums):
        def findtwosum(l, r, twosum):
            res = []
            while l < r:
                if nums[l]+nums[r] == twosum:
                    # 去重
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # 去重
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    res.append([-twosum, nums[l], nums[r]])
                    l += 1
                    r -= 1
                # 结果大了，r左移
                elif nums[l] + nums[r] > twosum:
                    r -= 1
                # 结果大了，l右移
                else:
                    l += 1
            return res

        if not nums or len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            # 排序后大于0 说明找不到 直接返回
            if nums[i] > 0:
                return res
            # 去重
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            res.extend(findtwosum(i+1, len(nums)-1, -nums[i]))
        return res

if __name__ == '__main__':
    print(Solution().threeSum([0,0,0]))