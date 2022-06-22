# 闭区间
# 1.左侧边界搜索
class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                r = mid - 1
        if l >= len(nums) or nums[l] != target:
            return -1
        return l

# 69
# https://leetcode.cn/problems/sqrtx/
# 和普通二分法不一样的地方就在于这道题找的值一定存在
# 更像是闭区间寻找一个数
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left,right = 0, x
        # 这里用小于可能因为mid可能是答案，所以搜索区间应该截止到[left,left],
        # 这样返回的时候可以返回left 说明此时left就是答案
        while left < right:
            # +1防止死循环
            mid = left + (right-left+1)//2
            if x/mid == mid:
                return mid
            elif x/mid > mid:
                # 这里的区间跟一般的二分查找不一样，因为此时mid可能是要找的答案 所以不能使用mid+1
                # [mid, right]
                left = mid
            elif x/mid < mid:
                # [left, mid-1]
                right = mid - 1
        return left

# 34.
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# 分开写
class Solution:
    def searchRange(self, nums,target: int):
        def bisearchleft(nums, target):
            l,r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] == target:
                    r = mid - 1
            if l >= len(nums) or nums[l] != target:
                return -1
            return l

        def bisearchright(nums, target):
            l,r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] == target:
                    l = mid + 1
            if l <= 0 or nums[l-1] != target:
                return -1
            return r
        l,r = bisearchleft(nums,target), bisearchright(nums,target)
        return [l,r]

# 合并写
class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1,-1]
        def bisearch(nums, target, left):
            l,r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target or (left and nums[mid] >= target):
                    r = mid - 1
                    ans = mid
                elif nums[mid] < target or (not left and nums[mid] <= target):
                    l = mid + 1

            if left and (l == len(nums) or nums[l] != target):
                return -1
            if not left and (l == 0 or nums[l-1] != target):
                return -1
            return l if left else r

        l,r = bisearch(nums,target,True), bisearch(nums,target,False)
        return [l,r]

if __name__ == '__main__':
    Solution().search([-1,0,3,5,9,12])




