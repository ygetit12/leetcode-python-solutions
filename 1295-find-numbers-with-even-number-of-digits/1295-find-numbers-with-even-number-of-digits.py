class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        c=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                c=c+1
        return c    