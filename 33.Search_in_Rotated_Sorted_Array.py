class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            # 在(mid, right]里找
            elif nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            # 在[left, mid)里找
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1