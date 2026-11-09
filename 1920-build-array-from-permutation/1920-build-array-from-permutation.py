class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        l=[]
        for i in range(0,len(nums)):
            l.append(nums[nums[i]])
        return l