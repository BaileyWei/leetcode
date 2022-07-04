# 46. permutations
from copy import deepcopy
class Solution:
    def permute(self, nums) :
        res = []
        def backtrack(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                backtrack(nums, deepcopy(tmp))
                tmp.pop()
        tmp = []
        backtrack(nums,tmp)
        return res