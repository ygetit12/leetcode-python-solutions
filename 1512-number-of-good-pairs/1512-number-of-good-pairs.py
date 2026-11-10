class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        c=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    c=c+1
        return c