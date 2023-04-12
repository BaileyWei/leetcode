class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(begin, end, nums):
            if begin > end:
                return nums
            i,j = begin,end
            rand = random.randint(begin, end)
            pivot = nums[rand]
            nums[i], nums[rand] = nums[rand], nums[i]
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[j] = pivot
            quickSort(begin, j-1, nums)
            quickSort(j+1, end, nums)
            return nums
        return quickSort(0, len(nums)-1, nums)




class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(begin, end, nums):
            if begin > end:
                return nums
            i,j = begin,end
            pivot = nums[i]
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            quickSort(begin, j-1, nums)
            quickSort(j+1, end, nums)
            return nums
        return quickSort(0, len(nums)-1, nums)