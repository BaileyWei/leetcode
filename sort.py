# quick sort
class Solution:
    def findKthLargest(self, nums, k) -> int:
        def quick_sort(begin, end, nums):
            if begin >= end:
                return nums
            i,j = begin,end
            pivot = nums[i]
            ## 随机的步骤
            # rand = random.randint(begin, end)
            # pivot = nums[rand]
            # nums[i], nums[rand] = nums[rand], nums[i]
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[j] = pivot
            quick_sort(begin, i-1, nums)
            quick_sort(i+1, end, nums)
            return nums
        return quick_sort(0, len(nums)-1, nums)[k-1]

if __name__ == '__main__':
    print(Solution().sortArray([3,2,1,5,6,4]))